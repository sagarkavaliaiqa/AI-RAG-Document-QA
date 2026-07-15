RAG MINPROJECT1/
│
├── app.py
├── config.py
├── utils.py
├── embeddings.py
├── vector_store.py
├── retriever.py
├── prompts.py
├── llm.py
├── requirements.txt
├── .env
│
├── Notes/
│   ├── 01_Streamlit.md
│   ├── 02_LangChain.md
│   ├── 03_FAISS.md
│   ├── 04_Embeddings.md
│   ├── 05_RAG_Flow.md
│   └── 06_Interview_QA.md
│
├── uploaded_docs/
├── vector_store/
└── .streamlit/
    └── config.toml

    What is Streamlit?
- Open-source Python framework
- Builds web applications with Python
- No HTML, CSS, or JavaScript required

Responsibilities
- Creates UI
- Runs a local web server
- Displays results
- Handles file uploads
- Handles user input

Common Components
- st.title()
- st.header()
- st.write()
- st.text_input()
- st.button()
- st.file_uploader()
- st.sidebar()
- st.spinner()
- st.success()
- st.error()

Run Command
streamlit run app.py

Configuration
.streamlit/config.toml