import faiss
import pickle
from sentence_transformers import SentenceTransformer

# Load chunks from previous step
with open("chunks.pkl", "rb") as f:
    chunks = pickle.load(f)

print("Chunks loaded:", len(chunks))

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

print("Creating embeddings...")

# 🧹 Step 1: Clean chunks
clean_chunks = []

for chunk in chunks:
    chunk = chunk.strip()

    if len(chunk) < 30:
        continue
    if "?" in chunk:
        continue
    if "Exercise" in chunk:
        continue
    if "Q." in chunk:
        continue

    clean_chunks.append(chunk)

print("Clean chunks:", len(clean_chunks))

# 🔧 Step 2: Create embeddings
embeddings = model.encode(clean_chunks)

# 🔧 Step 3: Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

# 💾 Step 4: Save index
faiss.write_index(index, "biology_index.faiss")

# 💾 Step 5: Save CLEAN chunks
with open("biology_chunks.pkl", "wb") as f:
    pickle.dump(clean_chunks, f)

print("Database saved!")