import logging
import time

from crewai.tools import tool
from llama_index.core import VectorStoreIndex, StorageContext
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.groq import Groq
from llama_index.core import Settings
import chromadb

from src.agents_src.config.agent_settings import AgentSettings

logger = logging.getLogger(__name__)

logger.info("Loading HuggingFace embedding model...")
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

DEFAULT_TOP_K = 3


def format_citation(meta: dict) -> str:
    file_name = meta.get("file_name") or meta.get("filename") or "Unknown file"
    page = meta.get("page_label") or meta.get(
        "page") or meta.get("page_number")
    if page is not None:
        return f"{file_name} p.{page}"
    return f"{file_name}"


@tool
def rag_query_tool(query: str) -> dict:
    """
    Answers a query by retrieving relevant documents and generating a response.
    Returns the generated answer, the source file names with the page if possible,
    the top score, and the confident. From which the information was retrieved.

    Args:
        query (str): The input query string to be processed.

    Returns:
        dict: A dictionary with the following keys:
            - 'answer': The generated answer string.
            - 'source': List of source file names and page (if possible) used for retrieval.

    Notes:
        - Requires properly configured AgentSettings and access to the vector store.
        - The function loads the embedding model and LLM each time it is called.
    """
    start_time = time.time()
    try:
        settings = AgentSettings()
        vector_store_path = settings.VECTOR_STORE_DIR
        collection_name = settings.COLLECTION_NAME

        # Configure LLM
        Settings.llm = Groq(
            model=settings.MODEL_NAME,
            temperature=settings.MODEL_TEMPERATURE,
            api_key=settings.GROQ_API_KEY,
        )

        # Load Chroma collection
        db = chromadb.PersistentClient(path=vector_store_path)
        chroma_collection = db.get_or_create_collection(collection_name)

        # connect to the vector store
        vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
        storage_context = StorageContext.from_defaults(
            vector_store=vector_store)
        # Load index from Chroma
        index = VectorStoreIndex.from_vector_store(
            vector_store=vector_store,
            storage_context=storage_context,
            embed_model=embed_model
        )
        # Create the query engine
        query_engine = index.as_query_engine(similarity_top_k=DEFAULT_TOP_K)
        # Pass the query to the query engine
        response = query_engine.query(query)

        source_nodes = getattr(response, "source_nodes", []) or []
        citations = []
        evidence = []

        for sn in source_nodes:
            node = getattr(sn, "node", None)
            if not node:
                continue
            meta = getattr(node, "metadata", {}) or {}
            citation = format_citation(meta)

            snippet = node.get_content()
            snippet = snippet.strip().replace("\n", " ")
            snippet = snippet[:600]

            citations.append(citation)
            evidence.append({"source": citation, "snippet": snippet})

        seen = set()
        citations = [c for c in citations if not (c in seen or seen.add(c))]

        seen_ev = set()
        dedup_evidence = []

        for e in evidence:
            key = (e['source'], e['snippet'])
            if key not in seen_ev:
                seen_ev.add(key)
                dedup_evidence.append(e)

        processing_time = round(time.time() - start_time, 2)
        logger.info(
            f"Query: {query}... | Time: {processing_time}s")

        return {
            "answer": response.response,
            "sources": citations,
            "evidence": dedup_evidence
        }
    except Exception as e:
        logger.error(f"RAG error: {e}", exc_info=True)
        return {
            "answer": "Technical error.",
            "sources": [],
            "evidence": [],
        }
