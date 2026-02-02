PDF-RAG-App-using-NVIDIA-NIM

A Streamlit-based Retrieval-Augmented Generation (RAG) application that ingests PDF documents, generates embeddings using NVIDIA NIM, stores them in a Chroma vector database, and enables context-aware question answering using NVIDIA-hosted large language models.

Overview

This project demonstrates how to build a document intelligence system where users can ask natural language questions and receive answers grounded strictly in the content of uploaded PDF files. The system combines high-quality embeddings, efficient vector search, and a powerful LLM to deliver accurate and reliable responses.

Key Features

• PDF document ingestion from a local directory
• Intelligent text chunking for better retrieval accuracy
• Embedding generation using NVIDIA nv-embed-v1
• Vector storage and semantic search using Chroma DB
• Context-aware question answering with DeepSeek v3.2 via ChatNVIDIA
• Transparent retrieval with visible document similarity results
• Simple and interactive Streamlit interface

Architecture Summary

The application loads PDF documents and splits them into manageable chunks.
Each chunk is converted into embeddings using NVIDIA NIM.
Embeddings are stored in a Chroma vector database for fast semantic retrieval.
When a user asks a question, the most relevant document chunks are retrieved and passed as context to the LLM.
The LLM generates answers strictly based on the retrieved context.

Technologies Used

Streamlit for user interface
LangChain for RAG orchestration
NVIDIA NIM for embeddings and LLM inference
Chroma DB for vector storage
DeepSeek v3.2 as the underlying language model

Use Cases

Document-based question answering
Enterprise knowledge base search
Research paper and report analysis
Internal documentation exploration
RAG system prototyping using NVIDIA infrastructure

Project Highlights

This project showcases an end-to-end RAG pipeline using NVIDIA’s AI ecosystem.
It demonstrates practical usage of embeddings, vector databases, and LLMs in a production-style application.
Designed to be modular, scalable, and suitable for real-world GenAI workflows.
