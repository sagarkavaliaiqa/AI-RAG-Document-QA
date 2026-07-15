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