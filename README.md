# 🚀 Enterprise Document RAG System

**Note: This is no AI coding challenge.** This is a fully hand-architected, production-ready RAG (Retrieval-Augmented Generation) system built from the ground up.

This project bridges the gap between raw machine learning models and end-user applications by implementing a decoupled, containerized architecture featuring a custom vector database, a high-performance backend, and an interactive frontend dashboard.

## 🏗️ Architecture & Tech Stack

*   **Frontend (UI):** [Streamlit](https://streamlit.io/) — Provides an interactive web dashboard for document uploads and chat interfaces.
*   **Backend (API):** [FastAPI](https://fastapi.tiangolo.com/) — Handles asynchronous HTTP routing, chunking logic, and real-time NDJSON streaming.
*   **Database (Vector Engine):** [PostgreSQL + pgvector](https://github.com/pgvector/pgvector) — Stores document embeddings and utilizes HNSW (Hierarchical Navigable Small World) indexing for lightning-fast semantic search.
*   **AI / Embeddings:** [Google GenAI SDK (Gemini)](https://ai.google.dev/) — Powers the LLM chat completions and `gemini-embedding-2` vectorization.
*   **Infrastructure:** [Docker Compose](https://docs.docker.com/compose/) — Orchestrates the entire application stack into isolated, interconnected containers.

## ✨ Core Features

*   **In-Memory Document Ingestion:** Upload `.pdf` or `.txt` files directly through the UI. The backend extracts, parses, and chunks the text entirely in memory using `pypdf` without leaving local footprints.
*   **Real-Time Data Streaming:** Utilizes a persistent HTTP connection and `requests.iter_lines()` to decode NDJSON chunks, creating a real-time "typewriter" effect in the UI.
*   **Conversational Memory:** Generates unique session UUIDs to track user state, allowing the AI to maintain context across continuous back-and-forth dialogue.
*   **Fully Containerized:** The database, API, and frontend are bound to a custom Docker bridge network, ensuring deterministic execution across any environment with a single command.
