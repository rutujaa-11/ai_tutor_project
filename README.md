📚 Biology AI Tutor 🤖

An AI-powered tutor that answers biology questions using textbook content. This project uses Retrieval-Augmented Generation (RAG) with FAISS and a transformer model to provide accurate and concise answers.

🚀 Features

* 🔍 Semantic search using FAISS
* 🧠 Context-aware answer generation
* 📖 Extracts answers from textbook content
* 🧹 Filters out irrelevant data (questions/exercises)
* ⚡ Fast and efficient response generation
* 🔧 Context compression using ScaleDown API

🏗️ Tech Stack
* Python
* Streamlit
* FAISS (Vector Database)
* Sentence Transformers
* HuggingFace Transformers (FLAN-T5)
* ScaleDown API

 🧠 How It Works

1. User enters a question
2. Question is converted into embeddings
3. FAISS retrieves relevant textbook chunks
4. Context is cleaned and filtered
5. ScaleDown API compresses the context
6. FLAN-T5 model generates the final answer

📂 Project Structure

├── app.py
├── biology_index.faiss
├── biology_chunks.pkl
├── chunks.pkl
├── create_vector_db.py
├── extract_text.py
├── README.md


⚙️ Installation & Setup

1. Install dependencies : -   pip install -r requirements.txt
2. Run the application : - streamlit run app.py

🧪 Example

Input : - What is circulatory system in humans?

Output : - The circulatory system in humans consists of the heart, blood, and blood vessels. It helps in transporting oxygen, nutrients, and waste materials throughout the body.                                                                                 
                                                                                                                                                                                                          📊 Results
                                                                                                                                                                                                                   • ⚡ Reduced answer time from minutes to seconds
• 📉 Context size reduced using compression
• ✅ Improved answer relevance
                                                                                                                                                                                                                  🌍 Real-World Applications
                                                                                                                                                                                                                                                      • E-learning platforms
• Digital textbooks
• AI-based study assistants
• Competitive exam preparation
                                                                                                                                                                                                                ⚠️ Challenges Faced
                                                                                                                                                                                                                    • API integration issues due to missing endpoint details
• Noisy data from textbook (questions, headings)
• Incomplete sentence generation
                                                                                                                                                                                                              💡 Future Improvements
                                                                                                                                                                                                                    • Improve chunking strategy
• Add support for multiple subjects
• Deploy as a web app
• Add voice-based interaction

📌 Conclusion

This project demonstrates how AI can enhance learning by providing quick and accurate answers from textbooks using modern NLP techniques.# ai_tutor_project
AI_TUTOR_PROJECT
