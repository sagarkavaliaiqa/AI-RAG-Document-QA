Examples:

What is RAG?
What is FAISS?
What are embeddings?
Why chunk documents?
Difference between RAG and fine-tuning?
Explain your project architecture.
Why did you use Streamlit?
Explain the retriever.
Explain vector databases.


What are environment variables?

Environment variables are configuration values stored outside the application code. They are commonly used for secrets such as API keys, database credentials, and configuration settings. In Python, we can load them from a .env file using load_dotenv() and access them with os.getenv(). This improves security and makes it easy to use different values in development, testing, and production without changing the source code.
1. import os
What is os?

os is a built-in Python module that lets your program interact with the operating system.

For interviews

If asked, "Which is better: Hugging Face or OpenAI Embeddings?", a balanced answer is:

"It depends on the project. For applications that need to run locally or process sensitive data, Hugging Face embeddings are a good choice because they can run without sending data to an external API. For cloud applications where managed services and high-quality hosted models are preferred, OpenAI embeddings are a common option. Both produce vector embeddings that can be stored in a vector database like FAISS or Pinecone for semantic search."

Q: What is the purpose of ollama pull llama3.1?

Answer:

The ollama pull llama3.1 command downloads the Llama 3.1 model from the Ollama model repository and stores it locally. Once downloaded, applications using ChatOllama(model="llama3.1") can load the model and perform inference on the local machine without downloading it again.





OPENAPI KEY USED INSTEAD OLLAMA WHAT CHANGES REQUIRED IN CODE
With OpenAI
1. Install the package
pip install langchain-openai
2. Create a .env file
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx
3. Load the API key
from dotenv import load_dotenv

load_dotenv()
4. Create the LLM
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini"
)

There is no ollama pull command because the model is not stored on your computer.

What happens internally?
Your RAG Application
        │
        ▼
OpenAI API
        │
        ▼
GPT-4o-mini (OpenAI Cloud)
        │
        ▼
Answer

The model runs on OpenAI's servers.

What if the API key is invalid?

You might see errors like:

401 Unauthorized

or

Incorrect API Key

or

429 Rate Limit Exceeded

Q: Why doesn't OpenAI require ollama pull?

Answer:

OpenAI models are hosted in the cloud. When we call ChatOpenAI, our application sends the prompt to OpenAI's servers over the internet. Since the model isn't stored locally, there's nothing to download. In contrast, Ollama runs models locally, so we first download the model with ollama pull and then run it on our own machine.

Interview answer:

LangChain is an orchestration framework for LLM applications. It helps integrate document loading, chunking, embeddings, vector databases, retrieval, prompt templates, and language models into a single RAG pipeline using reusable components.
Interview Answer

Q: How do you decide what goes into .gitignore?

Answer:

I include files and folders that are either generated automatically, contain sensitive information, or are specific to my local machine. For example, I ignore .env because it contains secrets, .venv because it can be recreated from requirements.txt, __pycache__ because Python generates it automatically, and runtime-generated folders like uploaded_docs and vector_store because they are created when the application runs. I commit only the source code, configuration needed by everyone, dependency list, and documentation.
Interview Question

Q: Why do we configure user.name and user.email in Git?

Answer:

Git records the author's name and email with every commit. This allows changes to be traced back to the developer who made them, which is useful for collaboration, code reviews, and maintaining project history.
✅ Built an end-to-end RAG application
✅ Used Python
✅ Used Streamlit
✅ Used LangChain
✅ Used FAISS
✅ Used Hugging Face Embeddings
✅ Integrated OpenAI/Ollama
✅ Learned Git
✅ Uploaded the project to GitHub
✅ Solved a real GitHub authentication issue

This is much stronger than just watching tutorials because you built and debugged the project yourself.

Is it useful for your resume?

Yes. Especially if you're targeting QA Automation + AI or SDET + GenAI roles.

You can add a project like this.

Project: End-to-End RAG Chatbot using LangChain

Technologies:

Python
Streamlit
LangChain
FAISS
Hugging Face Embeddings
OpenAI/Ollama
Git & GitHub

Description:

Developed an end-to-end Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents, generate embeddings, store vectors in FAISS, retrieve relevant document chunks, and answer user questions using an LLM through an interactive Streamlit interface.

Interview Questions You Can Expect
Project Overview
What is RAG?
Why did you build this project?
Explain the architecture.
Walk me through your application.
Python
Why did you use Python?
Explain virtual environments.
What is requirements.txt?
Why use .env?
Streamlit
Why Streamlit?
How does Streamlit rerun your script?
How do you upload PDFs?
LangChain
What is LangChain?
What is a Retriever?
What is a Vector Store?
What is a Chain?
Embeddings
What are embeddings?
Why not search raw text?
Which embedding model did you use?
FAISS
What is FAISS?
Why FAISS?
How are vectors stored?
Chunking
Why split PDFs into chunks?
What chunk size did you use?
What happens if chunks are too large?
LLM
Which LLM did you use?
Why OpenAI/Ollama?
What is temperature?
What is context length?
Git & GitHub
Explain git add.
Explain git commit.
Explain git push.
What is .gitignore?
What is a Git remote?
Tell me about the GitHub authentication issue you solved.
Scenario Questions
What happens when a user uploads a PDF?
How is the answer generated?
How would you support multiple PDFs?
How would you improve retrieval accuracy?
How would you deploy this application?
What are the limitations of your current solution?
streamlit run app.py
sagarkavali88@gmail.com
Kavali@2026
sagarkavali88-hub---->GITHUB USER NAME