import streamlit as st
from sentence_transformers import SentenceTransformer, util
import json

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load KB
with open("knowledge_base.json", "r") as f:
    knowledge_base = json.load(f)

questions = list(knowledge_base.keys())
question_embeddings = model.encode(questions, convert_to_tensor=True)

def get_answer(query, threshold=0.6):
    user_embedding = model.encode(query, convert_to_tensor=True)
    similarities = util.cos_sim(user_embedding, question_embeddings)[0]
    
    best_score = float(similarities.max())
    best_idx = int(similarities.argmax())
    
    if best_score >= threshold:
        matched_question = questions[best_idx]
        return knowledge_base[matched_question]
    else:
        return "❌ Sorry, I couldn't find a semantic match. Try rephrasing your question."

# Streamlit UI
st.set_page_config(page_title="CLAT Semantic Chatbot", page_icon="📚")
st.title("📘 CLAT Semantic Chatbot")
st.write("Ask me anything about CLAT 2025!")

user_input = st.text_input("Enter your question:")

if user_input:
    with st.spinner("Understanding your question..."):
        response = get_answer(user_input)
        st.success("Answer:")
        st.markdown(response)
