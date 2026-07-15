import os
from dotenv import load_dotenv

load_dotenv()

# Folder Paths
UPLOAD_FOLDER = "uploaded_docs"
VECTOR_STORE_PATH = "vector_store"

# Embedding Settings
# Embedding Model
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# Retrieval Settings
TOP_K = 3

# Model Settings
#MODEL_NAME = "gpt-4o-mini"

# API Keys
#OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# config.py

PAGE_TITLE = "RAG Chatbot"
PAGE_ICON = "🤖"

#MODEL_NAME = "gpt-4o-mini"
PAGE_TITLE = "RAG Chatbot"
PAGE_ICON = "📘"
LAYOUT = "wide"

MODEL_NAME = "llama3.1"