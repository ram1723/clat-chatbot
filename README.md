
# 📘 CLAT Chatbot – NLTI Internship Assignment (Task 2)

A smart chatbot that answers CLAT-related questions using semantic search (NLP). Built using Python, Streamlit, and Sentence Transformers.

## 🎯 Objective

Build a rule-based or NLP-powered chatbot to help CLAT aspirants with exam-related queries.

## ✅ Features

- Answer questions about CLAT syllabus, marking scheme, cut-offs, and more.
- Understands natural language queries using semantic similarity (SentenceTransformers).
- Lightweight and interactive web app built using Streamlit.
- Easily extendable via `knowledge_base.json`.

## 🧠 Architecture

- QnAs are stored in a modular JSON format.
- firstly tweaked with nlp technique of fuzzywuzzy ratios to give answers.
- Then,SentenceTransformer model `all-MiniLM-L6-v2` encodes both queries and stored questions.
- Uses cosine similarity to find the most semantically relevant match.
- Optional fallback to fuzzy matching available.
- Web interface built using Streamlit.

## 🚀 How to Run Locally

1. Clone or unzip the repository.
2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the chatbot:

```
streamlit run clat_chatbot_app.py
```

## 💡 Example Questions

- "How do I apply for CLAT?"
- "What is the marking pattern?"
- "When is the exam held?"
- "What’s the syllabus for 2025?"

## 🔁 How It Can Be Scaled to a GPT-Based Model

To scale this chatbot to a GPT-powered assistant fine-tuned on NLTI's content:

1. **Data Preparation**: Collect FAQs, mock interviews, guidance documents, and relevant legal study material from NLTI.
2. **Model Selection**: Start with an open-source LLM like GPT-2, GPT-Neo, or fine-tune GPT-3.5 via OpenAI's fine-tuning endpoint.
3. **Fine-tuning**: Use instruction-based QnA format to teach the model how to answer domain-specific queries.
4. **Evaluation**: Test using real aspirant queries and compare performance with current semantic search.
5. **Deployment**: Host the fine-tuned model with a fallback to the semantic search model for robustness.

## 📦 Future Improvements

- Integrate CLAT past paper and PDF search capabilities.
- Add user feedback and response improvement loop.
- Support for voice queries and mobile-friendly UI.




## 🔍 **Alternative Approach: Web Scraping + RAG with FAISS**
As an additional experiment, I explored a Retrieval-Augmented Generation (RAG) approach by integrating real-time data from the NLTI website.

## 🔹 What This Approach Does
Scrapes the homepage of NLTI to extract all post links and important dates.

Embeds this data using vector embeddings and stores them in a FAISS vector database.

At query time, uses a RAG chain to retrieve the most relevant chunks from the scraped data.

Feeds the results into an LLM (like GPT-4) to generate contextual responses.

## 🛠️ Implementation Files
app.py – the main Streamlit app entry point.

rag_utils.py – utilities for scraping, embedding, and retrieval.

## ▶️ To Run This Version
Run the chatbot:

```
streamlit run app.py
```
## 🚀 Future Enhancements
Swap current embeddings with OpenAI Embeddings for better semantic capture.

Use GPT-4 or Claude for more context-aware answers.

Extend scraping to cover other NLTI sections (e.g., mentors, FAQ, blog, success stories).
```
## 🧑‍💻 Author

Developed as part of the NLTI Internship Assignment – Task 2
The working and explanation video is also uploaded in the repo
