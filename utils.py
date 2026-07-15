# utils.py

import os

def save_pdf(uploaded_file):

    os.makedirs("uploaded_docs", exist_ok=True)

    pdf_path = os.path.join(
        "uploaded_docs",
        uploaded_file.name
    )

    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return pdf_path

from langchain_community.document_loaders import PyPDFLoader

def load_pdf(pdf_path):

    loader = PyPDFLoader(pdf_path)

    return loader.load()
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import *

def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    return splitter.split_documents(documents)
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import *

def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    return splitter.split_documents(documents)
from config import CHUNK_SIZE, CHUNK_OVERLAP

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP
)