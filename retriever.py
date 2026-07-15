from config import TOP_K

def retrieve_documents(vector_store, question):
    return vector_store.similarity_search(
        question,
        k=TOP_K
    )
