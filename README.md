
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

## 🧑‍💻 Author

Developed as part of the NLTI Internship Assignment – Task 2
The working and explanation video is also uploaded in the repo


##**The other approach**
This approach is of **scraping the webpage of NLTI** and obtain all the **postings links** available or posted on the home page..along with the **important dates** mentioned in the home page.
These are embedded and stored in the vector database(FAISS) to build an **RAG chain** for retirval purposes
then parsed through the LLMs to generate a response of the query being asked by the user.
for increasing accuracy we can consider using OpenAi embeddings and gpt4
**The files under them are:**
1-> app.py
2->rag_utils.py

 Run the chatbot:

```
streamlit run app.py
```
