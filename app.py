import os
import streamlit as st
import time

from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings, ChatNVIDIA
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from langchain_community.vectorstores import FAISS, Chroma
from langchain_community.document_loaders import PyPDFDirectoryLoader

from dotenv import load_dotenv
load_dotenv()
os.environ['NVIDIA_API_KEY'] = os.getenv("NVIDIA_API_KEY")


def vector_embedding():

    if "vectors" not in st.session_state:

        st.session_state.embeddings = NVIDIAEmbeddings(
            model="nvidia/nv-embed-v1"
        )

        st.session_state.loader = PyPDFDirectoryLoader("./pdfs")
        st.session_state.docs = st.session_state.loader.load()

        st.session_state.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=100
        )

        st.session_state.final_documents = st.session_state.text_splitter.split_documents(
            st.session_state.docs[:30]
        )

        print("hEllo")

        st.session_state.vectors = Chroma.from_documents(
            st.session_state.final_documents,
            st.session_state.embeddings,
            persist_directory="./chroma_db"
        )


st.title("Nvidia NIM Demo")

llm = ChatNVIDIA(
    model="deepseek-ai/deepseek-v3.2"
)

prompt = ChatPromptTemplate.from_template(
"""
Answer the questions based on the provided context only.
Please provide the most accurate response based on the question
<context>
{context}
</context>
Questions:{input}
"""
)

prompt1 = st.text_input("Enter Your Question From Doduments")


if st.button("Documents Embedding"):
    vector_embedding()
    st.write("Vector Store DB Is Ready")


# -------------------- RAG (Runnable Style) --------------------

if prompt1 and "vectors" in st.session_state:

    retriever = st.session_state.vectors.as_retriever()

    rag_chain = (
        {
            "context": retriever,
            "input": RunnablePassthrough()
        }
        | prompt
        | llm
    )

    start = time.process_time()
    response = rag_chain.invoke(prompt1)
    print("Response time :", time.process_time() - start)

    st.write(response.content)

    with st.expander("Document Similarity Search"):
        docs = retriever.get_relevant_documents(prompt1)
        for doc in docs:
            st.write(doc.page_content)
            st.write("--------------------------------")
