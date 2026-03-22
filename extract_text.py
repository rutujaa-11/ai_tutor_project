import pdfplumber
import pickle

text = ""

# 📖 Extract text
with pdfplumber.open("Biology_science_book.pdf.pdf") as pdf:
    for page in pdf.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

# 🧹 Step 1: Basic cleaning
lines = text.split("\n")

clean_lines = []

for line in lines:
    line = line.strip()

    # ❌ skip unwanted lines
    if len(line) < 20:
        continue
    if "Exercise" in line:
        continue
    if "Q." in line:
        continue
    if line.endswith("?"):
        continue

    clean_lines.append(line)

# 🔗 Step 2: Merge lines into paragraphs
clean_text = " ".join(clean_lines)

# ✂ Step 3: Smart chunking (sentence-based)
sentences = clean_text.split(". ")

chunks = []
current_chunk = ""

for sentence in sentences:
    if len(current_chunk) + len(sentence) < 400:
        current_chunk += sentence + ". "
    else:
        chunks.append(current_chunk.strip())
        current_chunk = sentence + ". "

# Add last chunk
if current_chunk:
    chunks.append(current_chunk.strip())

print("Total clean chunks:", len(chunks))

# Preview
for i in range(min(3, len(chunks))):
    print(f"\n--- Chunk {i+1} ---")
    print(chunks[i])

# 💾 Save
with open("chunks.pkl", "wb") as f:
    pickle.dump(chunks, f)

print("Clean chunks saved!")