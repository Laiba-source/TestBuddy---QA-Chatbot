import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load pre-trained sentence embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load your Q&A knowledge base
with open('qa_knowledge.json') as f:
    data = json.load(f)

# Extract questions and compute embeddings
questions = [item['question'] for item in data]
vectors = model.encode(questions)

# Create FAISS index and store the vectors
index = faiss.IndexFlatL2(len(vectors[0]))
index.add(np.array(vectors))

# Save the index and questions for retrieval later
faiss.write_index(index, "vector_index.faiss")
np.save("questions.npy", questions)

print("✅ Embedding completed and saved successfully!")
