# 🌱 AgriProof AI: Evidence-Grounded Agricultural Intelligence

## 🎯 Overview

AgriProof AI is an **Agentic RAG (Retrieval-Augmented Generation)** system designed to revolutionize how agricultural knowledge is accessed and utilized. Instead of manually searching through hundreds of pages of agricultural documents or relying on simple keyword searches (Ctrl + F), users can ask natural language questions and receive:

- ✅ **Accurate, grounded answers** based on source documents
- 📝 **Clear, concise summaries** of complex information
- 🎯 **Structured key points** for quick understanding
- 🔍 **Exact evidence snippets** extracted directly from PDFs
- 📚 **Source citations** for full transparency

By providing **transparency** and **source attribution**, AgriProof AI reduces hallucinations and increases trust in AI-generated agricultural guidance.

---

## ✨ Features

### Core Capabilities

- **🤖 Multi-Agent Architecture**: Two specialized AI agents working in tandem
  - **Agent 1 (RAG QA Agent)**: Retrieves relevant, grounded information from agricultural PDFs
  - **Agent 2 (Summarization Agent)**: Synthesizes retrieved evidence into concise summaries and key points

- **📄 PDF Document Processing**: Automatically ingests and processes agricultural documents
  - Efficient chunking and embedding generation
  - Vector storage for fast semantic search
  - Support for multiple document formats

- **🔍 Evidence-Based Responses**: Every answer is backed by exact text from source documents
  - View the exact snippets used to generate answers
  - Full source attribution and citations
  - Transparent retrieval process

- **💬 Interactive Chat Interface**: User-friendly Streamlit-based frontend
  - Natural language question input
  - Structured response display
  - Expandable evidence viewers
  - Conversation history management

- **🚀 Production-Ready**: Containerized and cloud-deployable
  - Docker support for easy deployment
  - FastAPI backend for high performance
  - Scalable architecture

### Use Cases

- 🌾 **Crop Management**: Get instant answers about planting, irrigation, and harvest practices
- 🌡️ **Climate Adaptation**: Access climate-smart agricultural practices
- 🐛 **Pest Control**: Find evidence-based pest management strategies
- 💧 **Water Management**: Learn about efficient irrigation techniques
- 📊 **Agricultural Research**: Quickly extract insights from research documents

---

## 🏗 Architecture

AgriProof AI follows an **Agentic RAG architecture** with clear separation of concerns:

```
┌─────────────────────────────────────────────────────────────────┐
│                         USER INTERFACE                           │
│                      (Streamlit Frontend)                        │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                        BACKEND API                               │
│                      (FastAPI Server)                            │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                      AGENT ORCHESTRATION                         │
│                         (CrewAI)                                 │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────────────┐        ┌─────────────────────┐        │
│  │   Agent 1: RAG QA   │───────▶│  Agent 2: Summary   │        │
│  │                     │        │                     │        │
│  │ - Query Processing  │        │ - Text Synthesis    │        │
│  │ - Retrieval         │        │ - Key Points        │        │
│  │ - Evidence Extract  │        │ - Source Citations  │        │
│  └─────────┬───────────┘        └─────────────────────┘        │
│            │                                                     │
│            ▼                                                     │
│  ┌─────────────────────────────────────────────────────┐       │
│  │              RAG QA TOOL                            │       │
│  │           (LlamaIndex Engine)                       │       │
│  └─────────────────────┬───────────────────────────────┘       │
└────────────────────────┼─────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                     VECTOR STORE                                 │
│                      (ChromaDB)                                  │
│                                                                  │
│  - Semantic Search                                              │
│  - Document Embeddings (HuggingFace)                            │
│  - Efficient Retrieval                                          │
└─────────────────────────────────────────────────────────────────┘
```

### Component Flow

1. **Document Ingestion** (`rag_doc_ingestion/`)
   - Loads PDF documents from `docs_dir/`
   - Chunks documents into semantic segments
   - Generates embeddings using HuggingFace models
   - Stores vectors in ChromaDB

2. **Query Processing** (`agents_src/`)
   - User submits natural language question
   - RAG QA Agent retrieves relevant document chunks
   - Extracts evidence snippets with source information
   - Passes evidence to Summarization Agent

3. **Response Generation** (`agents_src/`)
   - Summarization Agent synthesizes information
   - Creates structured summary
   - Generates key points
   - Formats sources and citations

4. **API & Frontend** (`backend_src/`, `frontend_src/`)
   - FastAPI serves the backend
   - Streamlit provides interactive UI
   - Displays responses with evidence transparency

---

## 🛠 Tech Stack

### Core Technologies

| Technology | Purpose | Version |
|------------|---------|---------|
| **Python** | Core Language | 3.11 |
| **FastAPI** | Backend API Framework | 0.116.1 |
| **Streamlit** | Frontend Interface | 1.49.1 |
| **LlamaIndex** | RAG Framework | ≥0.14.0 |
| **CrewAI** | Multi-Agent Orchestration | 0.186.1 |
| **ChromaDB** | Vector Database | 1.0.21 |
| **PyTorch** | ML Framework (CPU) | 2.2.2 |

### Key Libraries

- **HuggingFace Embeddings**: For document vectorization
- **Groq LLM**: Language model provider (llama-3.3-70b-versatile)
- **Pydantic**: Data validation and settings management
- **Uvicorn**: ASGI server for FastAPI

### Infrastructure

- **Docker**: Containerization
- **AWS EC2**: Cloud deployment
- **Git**: Version control

---

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.11** or higher
- **pip** (Python package manager)
- **Docker** (optional, for containerized deployment)
- **Git** (for cloning the repository)
- **Groq API Key** ([Get one here](https://console.groq.com/))

### System Requirements

- **RAM**: Minimum 4GB (8GB+ recommended)
- **Storage**: At least 5GB free space
- **OS**: Linux, macOS, or Windows with WSL

---

## 🚀 Installation

### Local Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/AgriProof-AI.git
   cd AgriProof-AI
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**
   
   Create a `.env` file in the root directory:
   ```bash
   cp env_template.txt .env
   ```
   
   Edit `.env` with your configuration:
   ```env
   GROQ_API_KEY="your_actual_groq_api_key_here"
   DOCUMENTS_DIR="./docs_dir"
   VECTOR_STORE_DIR="./doc_vector_store"
   COLLECTION_NAME="document_collection"
   MODEL_NAME="llama-3.3-70b-versatile"
   MODEL_TEMPERATURE=0.0
   CHAT_ENDPOINT_URL="http://localhost:8000/chat/answer"
   ```

5. **Add Your Documents**
   
   Place your agricultural PDF documents in the `docs_dir/` folder:
   ```bash
   # Example structure
   docs_dir/
   ├── ClimateAg.pdf
   ├── CropProduction.pdf
   └── GAP(Manual).pdf
   ```

6. **Run Document Ingestion** (First Time Only)
   ```bash
   python -m src.rag_doc_ingestion.ingest_docs
   ```
   
   This will:
   - Load all PDFs from `docs_dir/`
   - Generate embeddings
   - Store vectors in ChromaDB

7. **Start the Backend API**
   ```bash
   uvicorn src.backend_src.main:app --host 0.0.0.0 --port 8000 --reload
   ```

8. **Start the Frontend** (In a new terminal)
   ```bash
   streamlit run src/frontend_src/app.py --server.port 8501
   ```

9. **Access the Application**
   
   Open your browser and navigate to:
   - Frontend: `http://localhost:8501`
   - API Docs: `http://localhost:8000/docs`

---

### Docker Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/AgriProof-AI.git
   cd AgriProof-AI
   ```

2. **Set Environment Variables**
   
   Edit the `Dockerfile` or create a `.env` file:
   ```env
   GROQ_API_KEY=your_actual_groq_api_key_here
   ```

3. **Build the Docker Image**
   ```bash
   docker build -t agriproof-ai:latest .
   ```

4. **Run the Container**
   ```bash
   docker run -d \
     --name agriproof-ai \
     -p 8000:8000 \
     -p 8501:8501 \
     -e GROQ_API_KEY="your_actual_groq_api_key_here" \
     -v $(pwd)/docs_dir:/app/docs_dir \
     -v $(pwd)/doc_vector_store:/app/doc_vector_store \
     agriproof-ai:latest
   ```

5. **Access the Application**
   - Frontend: `http://localhost:8501`
   - API: `http://localhost:8000`

6. **View Logs**
   ```bash
   docker logs -f agriproof-ai
   ```

7. **Stop the Container**
   ```bash
   docker stop agriproof-ai
   docker rm agriproof-ai
   ```

---

### AWS EC2 Deployment

1. **Launch EC2 Instance**
   - AMI: Ubuntu 22.04 LTS
   - Instance Type: t3.medium or larger
   - Storage: 20GB+ EBS volume
   - Security Group: Allow ports 22, 8000, 8501

2. **Connect to Instance**
   ```bash
   ssh -i your-key.pem ubuntu@your-ec2-ip
   ```

3. **Install Docker**
   ```bash
   sudo apt update
   sudo apt install -y docker.io docker-compose
   sudo usermod -aG docker ubuntu
   newgrp docker
   ```

4. **Clone and Deploy**
   ```bash
   git clone https://github.com/yourusername/AgriProof-AI.git
   cd AgriProof-AI
   
   # Build and run
   docker build -t agriproof-ai .
   docker run -d \
     --name agriproof-ai \
     -p 8000:8000 \
     -p 8501:8501 \
     -e GROQ_API_KEY="your_key" \
     --restart unless-stopped \
     agriproof-ai
   ```

5. **Access Remotely**
   - Frontend: `http://your-ec2-ip:8501`
   - API: `http://your-ec2-ip:8000`

6. **Set Up Domain (Optional)**
   - Configure Route 53 or your DNS provider
   - Point domain to EC2 elastic IP
   - Set up NGINX reverse proxy with SSL

---

## ⚙️ Configuration

### Environment Variables

All configuration is managed through environment variables. Here's a complete reference:

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `GROQ_API_KEY` | Your Groq API key for LLM access | - | ✅ Yes |
| `DOCUMENTS_DIR` | Path to PDF documents directory | `./docs_dir` | No |
| `VECTOR_STORE_DIR` | Path to ChromaDB storage | `./doc_vector_store` | No |
| `COLLECTION_NAME` | ChromaDB collection name | `document_collection` | No |
| `MODEL_NAME` | Groq model to use | `llama-3.3-70b-versatile` | No |
| `MODEL_TEMPERATURE` | LLM temperature (0.0-1.0) | `0.0` | No |
| `CHAT_ENDPOINT_URL` | Backend API endpoint | `http://localhost:8000/chat/answer` | No |

### Supported Groq Models

- `llama-3.3-70b-versatile` (Recommended - Best for RAG)
- `llama-3.1-70b-versatile`
- `mixtral-8x7b-32768`

### Customizing Agent Behavior

Edit agent configurations in `src/agents_src/config/agent_settings.py`:

```python
# Example: Adjust retrieval parameters
TOP_K = 5  # Number of chunks to retrieve
CHUNK_SIZE = 512  # Size of document chunks
```

---

## 📖 Usage

### Basic Workflow

1. **Start the Application**
   ```bash
   # Terminal 1: Backend
   uvicorn src.backend_src.main:app --host 0.0.0.0 --port 8000
   
   # Terminal 2: Frontend
   streamlit run src/frontend_src/app.py
   ```

2. **Ask Questions**
   
   Navigate to `http://localhost:8501` and start asking questions:
   
   **Example Questions:**
   - "What are the best irrigation practices for rice cultivation?"
   - "How does climate change affect wheat production?"
   - "What are integrated pest management strategies for tomatoes?"
   - "Explain the principles of sustainable agriculture"

3. **Review Responses**
   
   Each response includes:
   - **Summary**: Concise answer to your question
   - **Key Points**: Bullet-pointed highlights
   - **Sources**: List of source documents
   - **Evidence Snippets**: Expandable view of exact text from PDFs

4. **Clear Conversation**
   
   Use the "Clear conversation" button in the sidebar to reset chat history

### Advanced Usage

#### Adding New Documents

1. Place PDF files in `docs_dir/`
2. Re-run ingestion:
   ```bash
   python -m src.rag_doc_ingestion.ingest_docs
   ```
3. Restart the application

#### Programmatic API Access

```python
import requests

response = requests.post(
    "http://localhost:8000/chat/answer",
    json={
        "chat_history": [
            {"role": "user", "content": "What is crop rotation?"}
        ]
    }
)

result = response.json()
print(result["summary"])
print(result["key_points"])
```

---

## 📚 API Documentation

### Base URL
```
http://localhost:8000
```

### Endpoints

#### POST `/chat/answer`

Processes user questions and returns AI-generated answers with evidence.

**Request Body:**
```json
{
  "chat_history": [
    {
      "role": "user",
      "content": "What are the benefits of crop rotation?"
    }
  ]
}
```

**Response:**
```json
{
  "summary": "Crop rotation offers multiple benefits including improved soil health, pest control, and increased yields...",
  "key_points": [
    "Improves soil nutrient balance",
    "Reduces pest and disease pressure",
    "Increases crop yields over time"
  ],
  "sources": [
    "CropProduction.pdf",
    "GAP(Manual).pdf"
  ],
  "evidence": [
    {
      "source": "CropProduction.pdf",
      "snippet": "Crop rotation is a proven practice that enhances soil fertility..."
    }
  ]
}
```

**Status Codes:**
- `200 OK`: Successful response
- `400 Bad Request`: Invalid input
- `500 Internal Server Error`: Processing error

### Interactive API Docs

FastAPI provides interactive documentation:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

---

## 📁 Project Structure

```
AgriProof-AI/
├── 📄 README.md                     # Project documentation
├── 📄 requirements.txt              # Python dependencies
├── 📄 Dockerfile                    # Docker configuration
├── 📄 .env                          # Environment variables (create from template)
├── 📄 .gitignore                    # Git ignore rules
├── 📄 .dockerignore                 # Docker ignore rules
├── 📄 start.sh                      # Startup script for Docker
├── 📄 env_template.txt              # Environment template
│
├── 📁 docs_dir/                     # Agricultural PDF documents
│   ├── ClimateAg.pdf
│   ├── CropProduction.pdf
│   └── GAP(Manual).pdf
│
├── 📁 doc_vector_store/             # ChromaDB vector storage
│   └── [generated automatically]
│
├── 📁 venv/                         # Python virtual environment
│
└── 📁 src/                          # Source code
    │
    ├── 📁 agents_src/               # Agent orchestration
    │   ├── __init__.py
    │   ├── crew.py                  # CrewAI orchestration
    │   │
    │   ├── 📁 agents/               # Agent definitions
    │   │   ├── __init__.py
    │   │   ├── question_answer_agent.py    # RAG QA Agent
    │   │   └── summarizer_agent.py         # Summarization Agent
    │   │
    │   ├── 📁 tasks/                # Agent tasks
    │   │   ├── __init__.py
    │   │   ├── question_answer_task.py
    │   │   └── summarizer_task.py
    │   │
    │   ├── 📁 tools/                # Agent tools
    │   │   ├── __init__.py
    │   │   └── rag_qa_tool.py      # RAG query tool
    │   │
    │   ├── 📁 llm/                  # LLM configuration
    │   │   ├── __init__.py
    │   │   ├── get_llm.py
    │   │   └── llm_configuration.py
    │   │
    │   └── 📁 config/               # Agent settings
    │       ├── __init__.py
    │       └── agent_settings.py
    │
    ├── 📁 backend_src/              # FastAPI backend
    │   ├── __init__.py
    │   ├── main.py                  # FastAPI app entry
    │   │
    │   ├── 📁 api/                  # API routes
    │   │   ├── __init__.py
    │   │   └── chat.py              # Chat endpoint
    │   │
    │   ├── 📁 services/             # Business logic
    │   │   ├── __init__.py
    │   │   └── chat.py
    │   │
    │   └── 📁 config/               # Backend settings
    │       ├── __init__.py
    │       └── backend_settings.py
    │
    ├── 📁 frontend_src/             # Streamlit frontend
    │   ├── __init__.py
    │   ├── app.py                   # Main Streamlit app
    │   │
    │   └── 📁 config/               # Frontend settings
    │       ├── __init__.py
    │       └── frontend_settings.py
    │
    └── 📁 rag_doc_ingestion/        # Document processing
        ├── __init__.py
        ├── ingest_docs.py           # PDF ingestion script
        │
        └── 📁 config/               # Ingestion settings
            ├── __init__.py
            └── doc_ingestion_settings.py
```

---

## 🔧 How It Works

### 1. Document Ingestion Pipeline

```python
# src/rag_doc_ingestion/ingest_docs.py

1. Load PDFs from docs_dir/
   ↓
2. Parse and chunk documents (512 tokens per chunk)
   ↓
3. Generate embeddings using HuggingFace (BAAI/bge-small-en-v1.5)
   ↓
4. Store in ChromaDB vector database
   ↓
5. Create searchable index
```

### 2. Query Processing Flow

```python
# User asks: "What is drip irrigation?"

1. Frontend sends question to Backend API
   ↓
2. Backend invokes Agent Crew
   ↓
3. RAG QA Agent activates:
   - Converts question to embedding
   - Performs semantic search in ChromaDB
   - Retrieves top-k relevant chunks
   - Extracts evidence snippets
   ↓
4. Summarization Agent activates:
   - Receives evidence from RAG QA Agent
   - Synthesizes information using Groq LLM
   - Generates structured summary
   - Formats key points
   - Compiles source citations
   ↓
5. Response sent to Frontend
   ↓
6. UI displays:
   - Summary
   - Key points
   - Sources
   - Evidence snippets (expandable)
```

### 3. Multi-Agent Collaboration

**Agent 1: RAG QA Agent**
- **Role**: Evidence retrieval specialist
- **Tools**: RAG Query Tool (LlamaIndex)
- **Responsibilities**:
  - Query understanding
  - Semantic search
  - Evidence extraction
  - Source tracking

**Agent 2: Summarization Agent**
- **Role**: Information synthesizer
- **Tools**: LLM (Groq)
- **Responsibilities**:
  - Content synthesis
  - Key point extraction
  - Summary generation
  - Source formatting

**Orchestration** (CrewAI):
- Sequential task execution
- Inter-agent communication
- Result aggregation
- Error handling

---

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

### Ways to Contribute

- 🐛 Report bugs
- 💡 Suggest new features
- 📝 Improve documentation
- 🔧 Submit pull requests
- 🌍 Add support for more languages
- 📚 Contribute agricultural documents

### Development Setup

1. **Fork the Repository**
   ```bash
   # Click "Fork" on GitHub, then:
   git clone https://github.com/YOUR_USERNAME/AgriProof-AI.git
   cd AgriProof-AI
   ```

2. **Create Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Changes**
   - Follow PEP 8 style guide
   - Add docstrings to functions
   - Write unit tests if applicable

4. **Test Changes**
   ```bash
   # Run the application
   ./start.sh  # or manual startup
   
   # Test your feature
   ```

5. **Commit and Push**
   ```bash
   git add .
   git commit -m "Add: your feature description"
   git push origin feature/your-feature-name
   ```

6. **Create Pull Request**
   - Go to GitHub and open a PR
   - Describe your changes
   - Link related issues


### Reporting Issues

When reporting bugs, please include:
- Python version
- Operating system
- Error messages and stack traces
- Steps to reproduce
- Expected vs actual behavior

---

---

## 🚀 Roadmap

### Current Version (v1.0)
- ✅ Multi-agent RAG system
- ✅ PDF document ingestion
- ✅ Evidence-based responses
- ✅ Streamlit frontend
- ✅ Docker deployment

### Planned Features (v2.0)
- 🔄 Support for more document formats (DOCX, TXT, etc.)
- 🌐 Multi-language support
- 📊 Analytics dashboard
- 🔐 User authentication
- 💾 Conversation history persistence
- 🎨 Enhanced UI/UX
- 📱 Mobile app

### Future Ideas
- 🗣️ Voice input support
- 📷 Image-based queries (e.g., plant disease detection)
- 🌍 Integration with agricultural APIs
- 🤖 Fine-tuned domain-specific models
- 📡 Real-time collaboration features

---

<div align="center">


**Happy Farming! 🌾**

</div>
