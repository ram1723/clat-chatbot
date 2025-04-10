# Setup
!apt update > /dev/null
!apt install chromium-chromedriver > /dev/null
!pip install selenium > /dev/null
import faiss
import pickle
from sentence_transformers import SentenceTransformer
import openai
import os

# Load FAISS index and associated data
def load_retriever(index_path="clat_faiss.index", data_path="retrieval_data.pkl"):
    index = faiss.read_index(index_path)
    with open(data_path, "rb") as f:
        chunks, metadata = pickle.load(f)
    return index, chunks, metadata

# Load embedding model
def get_embedder():
    return SentenceTransformer("all-MiniLM-L6-v2")

# Simple top-k vector search
def retrieve_top_k(query, index, chunks, metadata, model, k=5):
    query_vec = model.encode([query])
    D, I = index.search(query_vec, k)

    results = []
    for i in I[0]:
        results.append({
            "chunk": chunks[i],
            "source": metadata[i]["source"]
        })
    return results

# Generate answer using OpenAI
def generate_answer(query, top_chunks):
    context = "\n\n".join([f"{c['chunk']}" for c in top_chunks])
    prompt = f"""You are an assistant for CLAT 2025 official updates.
Use the following context to answer the user's query. Be concise and accurate.

Context:
{context}

User Query:
{query}

Answer:"""
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        max_tokens=400
    )
    
    return response.choices[0].message.content.strip()
