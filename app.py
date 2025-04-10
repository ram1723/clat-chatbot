import streamlit as st
from rag_utils import load_retriever, get_embedder, retrieve_top_k, generate_answer

st.set_page_config(page_title="CLAT Assistant", layout="wide")
st.title("📚 CLAT 2025 RAG Assistant")

with st.sidebar:
    st.subheader("🔑 API Key")
    openai_api_key = st.text_input("Enter your OpenAI API Key", type="password")

    st.markdown("---")
    st.markdown("Made with ❤️ for CLAT Aspirants")

# Load retriever
@st.cache_resource
def setup():
    index, chunks, metadata = load_retriever()
    model = get_embedder()
    return index, chunks, metadata, model

index, chunks, metadata, model = setup()

# Query input
query = st.text_input("Ask me anything related to CLAT 2025...")

if query and openai_api_key:
    with st.spinner("🔍 Retrieving relevant info..."):
        top_chunks = retrieve_top_k(query, index, chunks, metadata, model)

    with st.spinner("🤖 Generating answer..."):
        response = generate_answer(query, top_chunks, openai_api_key)

    st.subheader("🧠 Answer")
    st.write(response)

    st.markdown("---")
    with st.expander("📄 Sources"):
        for c in top_chunks:
            st.markdown(f"- **From:** {c['source']}")
            st.code(c["chunk"][:500] + ("..." if len(c["chunk"]) > 500 else ""))
