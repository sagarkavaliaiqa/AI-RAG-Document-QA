import streamlit as st

from config import *
from utils import save_pdf, load_pdf, split_documents
from embeddings import get_embeddings
from vector_store import create_vector_store
from retriever import retrieve_documents
from llm import get_llm
from prompts import RAG_PROMPT
from config import PAGE_TITLE, PAGE_ICON, MODEL_NAME
# =====================================================
# STREAMLIT PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title=PAGE_TITLE,
    layout=LAYOUT
)

st.title("📘 PDF RAG Chatbot")
st.write("Upload a PDF and build a Vector Database")

# =====================================================
# FILE UPLOAD
# =====================================================

# =====================================================
# FILE UPLOAD
# =====================================================

from config import UPLOAD_FOLDER

save_path = UPLOAD_FOLDER

uploaded_file = st.file_uploader(
    "Upload your PDF",
    type=["pdf"]
)

# =====================================================
# PROCESS PDF
# =====================================================

if uploaded_file:

    # Save PDF
    pdf_path = save_pdf(uploaded_file)

    st.success("✅ PDF Uploaded Successfully")

    # Load PDF
    documents = load_pdf(pdf_path)

    st.success("✅ PDF Loaded Successfully")

    st.write("Total Pages:", len(documents))

    # Display First Page
    st.subheader("📄 First Page")
    st.write(documents[0].page_content)

    # Split PDF
    chunks = split_documents(documents)

    st.success("✅ PDF Split Successfully")
    st.write("Total Chunks:", len(chunks))

    # Display First Chunk
    st.subheader("📄 First Chunk")
    st.write(chunks[0].page_content)

    # Create Embeddings
    embeddings = get_embeddings()

    st.success("✅ Embeddings Created")

    # Create FAISS Vector Store
    vector_store = create_vector_store(
        chunks,
        embeddings
    )

    st.success("✅ FAISS Vector Database Created")
    st.write("Total Vectors:", len(chunks))

    # Load LLM
    llm = get_llm()

    st.success("🎉 Your RAG Vector Database is Ready!")

    # =====================================================
    # CHAT SECTION
    # =====================================================

    st.divider()

    st.header("💬 Chat with your PDF")

    question = st.text_input(
        "Ask a question about your PDF"
    )

    if question:

        # Retrieve similar chunks
        docs = retrieve_documents(
            vector_store,
            question
        )

        # Build context
        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        # Create Prompt
        prompt = RAG_PROMPT.format(
            context=context,
            question=question
        )

        # Ask LLM
        response = llm.invoke(prompt)

        # Display Answer
        st.subheader("🤖 Answer")
        st.write(response.content)

        # Display Retrieved Chunks
        with st.expander("📄 Retrieved Chunks"):

            for i, doc in enumerate(docs, start=1):
                st.markdown(f"### Chunk {i}")
                st.write(doc.page_content)
                