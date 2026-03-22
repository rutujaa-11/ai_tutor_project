•  🏗️ Project Architecture

• Overview
Biology AI Tutor is an AI-based system that answers user questions using textbook data.  
It follows a Retrieval-Augmented Generation (RAG) approach, where relevant information is retrieved first and then used by a language model to generate answers.

•  Components
 
 1. User Interface (Streamlit)
The frontend of the application is built using Streamlit.  
Users can enter their biology-related questions through a simple web interface.

 2. Embedding Model
Model Used: all-MiniLM-L6-v2  

This model converts text into numerical vectors (embeddings).  
Both the user query and textbook content are converted into embeddings for similarity comparison.

 3. Vector Database (FAISS)
FAISS is used to store embeddings of textbook chunks.  

When a query is entered:
- The query is converted into an embedding  
- FAISS searches for the most similar chunks  

 4. Retrieval System
Top 3 most relevant chunks are retrieved based on similarity score.  
Unwanted content such as questions and exercises is filtered out.

 5. Prompt Creation
A structured prompt is created by combining:
- Instructions
- Retrieved context
- User question  

6. Language Model
Model Used: google/flan-t5-base  

This model generates the final answer using the provided context and question.

Workflow
User → Query → Embedding → FAISS Search → Context Retrieval → Prompt → LLM → Answer