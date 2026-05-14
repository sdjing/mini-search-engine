# Mini Search Engine

A document search engine that indexes local text files and ranks results using BM25 scoring. Built to demonstrate core information retrieval concepts including tokenization, stemming, and relevance ranking.

## Features
- Indexes any collection of local text documents
- BM25 relevance scoring for accurate result ranking
- NLTK preprocessing (stopword removal, stemming)
- Streamlit search interface with result snippets and scores

## Tech Stack
- Python
- NLTK
- rank-bm25
- scikit-learn
- Streamlit

## Setup

1. Clone the repo
```
git clone https://github.com/sdjing/mini-search-engine.git
cd mini-search-engine
```

2. Install dependencies
```
pip install -r requirements.txt
```

3. Add documents to the `docs/` folder as `.txt` files

4. Run the app
```
python -m streamlit run search_app.py
```

## Usage
1. Add any `.txt` files to the `docs/` folder
2. Run the app — documents are indexed automatically on startup
3. Type a query into the search bar
4. Results are ranked by BM25 score with a preview snippet
