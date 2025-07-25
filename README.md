# Information-Retrieval-System

This project is an AI-powered Information Retrieval System designed to help students, researchers, and professionals extract accurate answers from large PDF documents through natural language queries. By leveraging LangChain, Cohere LLMs, vector databases (FAISS), and Streamlit, the system enables real-time, conversational question answering without requiring manual keyword search.

# How to run?

STEPS:

1) Clone the repository:

   Project repo: https://github.com/
2) Create a conda environment after opening the repository:

   conda create -n genai python=3.9 -y

   conda activate genai
3) install the requirements:

   pip install -r requirements.txt

4) Create a .env file in the root directory and add your COHERE_API_KEY as follows:

   COHERE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
5) Finally run the following command:

   streamlit run app.py

# Output:
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/4a1db5a6-ec36-4d98-9846-3c702390e155" />


