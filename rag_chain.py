# rag_chain.py

from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama

def load_and_split_pdf(pdf_path):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(documents)
    return chunks


def create_faiss_vectorstore(chunks):
    embeddings = HuggingFaceEmbeddings()  # Uses sentence-transformers by default
    vectorstore = FAISS.from_documents(chunks, embeddings)
    return vectorstore


def build_rag_chain(vectorstore):
    retriever = vectorstore.as_retriever()
    llm = Ollama(model="mistral")  # Make sure you've pulled it via `ollama pull mistral`
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa_chain


def answer_question_from_pdf(pdf_path, user_query):
    chunks = load_and_split_pdf(pdf_path)
    vectorstore = create_faiss_vectorstore(chunks)
    rag_chain = build_rag_chain(vectorstore)
    return rag_chain.run(user_query)



