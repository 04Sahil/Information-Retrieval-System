import streamlit as st
from src.helper import get_pdf_text, get_text_chunks, get_vector_store, get_conversational_chain
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="📄 PDF Q&A with Cohere", layout="wide")
st.title("📄 Chat with Your PDF using LangChain + Cohere")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = None

def user_input(user_question):
    chain = st.session_state.conversation
    response = chain.invoke({
        "question": user_question,
        "chat_history": st.session_state.chat_history or []
    })
    st.session_state.chat_history = response["chat_history"]
    st.write("🤖", response["answer"])

def main():
    user_question = st.text_input("Ask a question about your PDF:")
    if user_question and st.session_state.get("conversation"):
        user_input(user_question)

    with st.sidebar:
        st.header("📄 Upload PDF Files")
        pdf_docs = st.file_uploader("Upload your PDFs", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_docs)
                chunks = get_text_chunks(raw_text)
                vectorstore = get_vector_store(chunks)
                st.session_state.conversation = get_conversational_chain(vectorstore)
                st.success("Documents embedded and chat is ready!")

main()
