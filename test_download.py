from sentence_transformers import SentenceTransformer

model_name = "sentence-transformers/all-MiniLM-L6-v2"

print("Downloading and loading the model...")
model = SentenceTransformer(model_name)
print("Model loaded successfully!")
