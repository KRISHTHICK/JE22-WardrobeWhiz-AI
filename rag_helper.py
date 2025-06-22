# rag_helper.py
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.llms.ollama import Ollama


def create_qa_chain(text):
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.create_documents([text])
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vector_store = FAISS.from_documents(docs, embeddings)
    retriever = vector_store.as_retriever()
    llm = Ollama(model="tinyllama")
    return RetrievalQA.from_chain_type(llm=llm, retriever=retriever)


def query_rag_chain(qa_chain, question):
    return qa_chain.run(question)
