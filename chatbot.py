import faiss
import numpy as np
import json
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')
index = faiss.read_index("vector_index.faiss")
questions = np.load("questions.npy", allow_pickle=True)

with open("qa_knowledge.json") as f:
    qa_data = json.load(f)

def get_answer(user_question):
    try:
        vector = model.encode([user_question])
        vector = np.array(vector).astype('float32')  # FAISS requires float32

        # Search for the top-1 closest question vector
        distances, indices = index.search(vector, k=1)
        best_match_index = indices[0][0]

        # Debug prints (remove after testing)
        print(f"User question: {user_question}")
        print(f"Best match index: {best_match_index}")
        print(f"Matched question: {questions[best_match_index]}")
        print(f"Answer: {qa_data[best_match_index]['answer']}")

        # Return the matched answer
        return qa_data[best_match_index]['answer']
    except Exception as e:
        print(f"Error in get_answer: {e}")
        return "Sorry, something went wrong while finding the answer."
