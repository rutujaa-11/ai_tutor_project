import streamlit as st
import faiss
import pickle
import requests
import json
from sentence_transformers import SentenceTransformer
from transformers import pipeline

# Page config
st.set_page_config(page_title="Biology AI Tutor", page_icon="📚", layout="centered")

# Title
st.title("📚 Biology AI Tutor 🤖")
st.write("Ask questions from your Biology textbook and get AI-powered answers!")

# Load models
@st.cache_resource
def load_models():
    index = faiss.read_index("biology_index.faiss")

    with open("biology_chunks.pkl", "rb") as f:
        chunks = pickle.load(f)

    embed_model = SentenceTransformer("all-MiniLM-L6-v2")

    generator = pipeline("text2text-generation", model="google/flan-t5-base")

    return index, chunks, embed_model, generator

index, chunks, embed_model, generator = load_models()

# Input
query = st.text_input("🔍 Enter your question:")

# Button
if st.button("Get Answer"):

    if query.strip() != "":

        # 🔍 Step 1: embedding
        query_embedding = embed_model.encode([query])

        # 🔎 Step 2: search best chunk
        distances, indices = index.search(query_embedding, k=3)

        # 🧹 Step 3: clean context
        context_parts = []

        for idx in indices[0]:
            if idx < len(chunks):
                chunk = chunks[idx]

                if "?" in chunk or "Exercise" in chunk or "Q." in chunk:
                    continue

                context_parts.append(chunk)

        # 👉 only best chunk
        context = context_parts[0] if context_parts else ""
        context = context.strip()

        if not context.endswith("."):
            context += "."

        # 🤖 Step 4: ScaleDown + Answer
        with st.spinner("🤔 Thinking..."):

            try:
                # 🔗 ScaleDown API
                url = "https://api.scaledown.xyz/compress/raw/"

                headers = {
                    "x-api-key": "yourapikey",   
                    "Content-Type": "application/json"
                }

                payload = {
                    "context": context,
                    "prompt": query,
                    "scaledown": {
                        "rate": "auto"
                    }
                }

                response = requests.post(url, headers=headers, data=json.dumps(payload))
                result = response.json()

                # ✅ compressed prompt
                compressed_prompt = result.get("compressed_prompt", "")

                # ⚠️ fallback
                if not compressed_prompt:
                    compressed_prompt = context

                # 🧠 final prompt
                final_prompt = f"""
You are a biology tutor.

Give a proper definition or explanation in 2-3 complete sentences.
Start the answer with the topic name.
Do NOT give one-word answers.

{compressed_prompt}
"""

                output = generator(
                    final_prompt,
                    max_length=150,
                    min_length=50,
                    do_sample=False
                )

                answer = output[0]["generated_text"]

            except Exception as e:
                answer = f"⚠️ Error: {str(e)}"

        # Output
        st.subheader("🧠 AI Answer:")
        st.success(answer)

        with st.expander("📖 Show Book Context"):
            st.write(context)

    else:
        st.warning("⚠️ Please enter a question!")