![image](https://github.com/user-attachments/assets/11fe77bf-6a74-4f4d-8628-01a459b37a4a)# TestBuddy - QA Chatbot

🧪 **TestBuddy** is an intelligent question-answering chatbot designed to assist with software testing-related queries. Built using Streamlit for the web interface, Sentence Transformers for semantic text embeddings, and FAISS for fast similarity search.

---

## Demo

![TestBuddy Demo]  



You can run the app locally or deploy it on [Streamlit Cloud](https://streamlit.io/cloud) to share a live version.

---

Features

- Semantic search-based question answering using Sentence Transformers and FAISS
- Simple and user-friendly web interface with Streamlit
- Supports software testing-related questions with accurate answers from a predefined knowledge base
- Lightweight and fast response time

---

 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/testbuddy-chatbot.git
   cd testbuddy-chatbot
Create and activate a virtual environment:

bash
Copy
Edit
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the Streamlit app:

bash
Copy
Edit
streamlit run app.py
Open your browser and go to http://localhost:8501 to use the chatbot.

Usage
Type your software testing question into the input box.

The chatbot will find the best matching answer from its knowledge base and display it.


Technologies Used
Python 3.x

Streamlit

Sentence Transformers (all-MiniLM-L6-v2)

FAISS

Numpy

JSON

Future Improvements
Add dynamic knowledge base updates without needing to rebuild index

Support multi-turn conversations

Deploy on cloud platform for public access

Enhance UI/UX with richer design and interactive elements

About Me
I am passionate about software testing and AI-powered tools. This chatbot project showcases my skills in Python, NLP, and building interactive web apps.

Contact
Feel free to reach out via adreesmuhammad540@gmail.com

