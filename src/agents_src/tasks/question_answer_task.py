from crewai import Task
from pydantic import BaseModel

from src.agents_src.agents.question_answer_agent import qa_agent


class AnswerStructure(BaseModel):
    answer: str
    sources: list[str]
    tool_used: str
    rationale: str
    evidence: list[dict]


qa_task = Task(
    agent=qa_agent,
    name="Question Answering Task",
    description="""
    Answer the user query "{user_query}" using a Retrieval-Augmented Generation (RAG) pipeline.
    chat_history: "{chat_history}"
    
    Instructions:
    - You MUST call `rag_query_tool`.
    - You MUST use ONLY the information supported by `sources` returned from the tool.
    - Retrieve relevant context from the document store
    - Prioritize evidence that directly addresses the query
    - Synthesize a clear, accurate answer grounded in the retrieved sources
    - If the query cannot be answered from the knowledge source, do not generate your own response.
      Instead, state clearly that the knowledge source does not contain the required information.
    - Provide transparency by including references, tool usage, and reasoning steps
    """,
    expected_output="""
    A structured JSON object with the following fields:
    {
      "answer": "Direct response to the query (1–3 paragraphs, clear and accurate). 
                 If no answer is found, return: 'The knowledge source does not contain the required information.'",
      "snippet": [
        {
          "text": "Exact quote from document",
          "source": "filename",
          "page": "page number",
        }
      ],
      "sources": ["List of document titles, sections, or citations, page number used (empty list if none)"],
      "tool_used": "Name of the retrieval/analysis tool invoked (e.g., RAG Retriever, VectorDB, ChatHistory, etc.)",
      "rationale": "Brief explanation of why this answer was chosen, or why no relevant information was found"
    }
    """,
    output_pydantic=AnswerStructure,
)
