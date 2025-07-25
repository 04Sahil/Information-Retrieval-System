import os
from PyPDF2 import PdfReader
from langchain_text_splitters import CharacterTextSplitter
from langchain_cohere import CohereEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain
from langchain_cohere import ChatCohere
from dotenv import load_dotenv

load_dotenv()

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        reader = PdfReader(pdf)
        for page in reader.pages:
            content = page.extract_text()
            if content:
                text += content
    return text

def get_text_chunks(text):
    splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=200, length_function=len)
    return splitter.split_text(text)

def get_vector_store(chunks):
    embeddings = CohereEmbeddings(model="embed-english-v2.0")
    return FAISS.from_texts(texts=chunks, embedding=embeddings)

def get_conversational_chain(vectorstore):
    llm = ChatCohere(model="command-r-plus")
    return ConversationalRetrievalChain.from_llm(llm=llm, retriever=vectorstore.as_retriever())
