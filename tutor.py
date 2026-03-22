import faiss
import pickle
from sentence_transformers import SentenceTransformer
from transformers import pipeline

# Load FAISS vector database
index = faiss.read_index("biology_index.faiss")

# Load text chunks
with open("biology_chunks.pkl", "rb") as f:
    chunks = pickle.load(f)

# Load embedding model
embed_model = SentenceTransformer("all-MiniLM-L6-v2")

# Load model (FLAN-T5 is good 👍)
model = pipeline("text2text-generation", model="google/flan-t5-base")

print("\n🧠 Biology AI Tutor Ready!")
print("Type your question (or type 'exit' to quit)\n")

while True:

    query = input("Ask: ")

    if query.lower() == "exit":
        print("Goodbye 👋")
        break

    # 🔍 Step 1: embedding
    query_embedding = embed_model.encode([query])

    # 🔎 Step 2: search top chunks
    distances, indices = index.search(query_embedding, k=3)

    # 🧹 Step 3: clean context (REMOVE QUESTIONS)
    context_parts = []

    for idx in indices[0]:
        if idx < len(chunks):
            chunk = chunks[idx]

            # ❌ skip exercise / questions
            if "?" in chunk or "Exercise" in chunk or "Q." in chunk:
                continue

            context_parts.append(chunk)

    # 👉 only best 2 chunks
    context = " ".join(context_parts[:2])
    context = context[:600]

    print("\n⚡ Generating answer...\n")

    try:
        # 🧠 IMPORTANT: proper prompt
        prompt = f"""
You are a biology tutor.

Answer the question using ONLY the given context.
Give a clear and short definition or explanation.
Do NOT include questions.

Context:
{context}

Question:
{query}

Answer:
"""

        result = model(
            prompt,
            max_length=120,
            do_sample=False
        )

        answer = result[0]["generated_text"]

    except Exception as e:
        answer = f"⚠️ Error: {str(e)}"

    print("📚 AI Answer:\n")
    print(answer)

    print("\n--------------------------------\n")