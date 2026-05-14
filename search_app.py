import streamlit as st
from indexer import load_documents, build_index
from search import build_bm25, search

DOCS_DIR = "docs"

st.set_page_config(page_title="Mini Search Engine", layout="centered")
st.title("Mini Search Engine")
st.caption("Searches and ranks documents using BM25 scoring.")

@st.cache_resource
def load_engine():
    docs = load_documents(DOCS_DIR)
    index = build_index(docs)
    bm25, filenames = build_bm25(index)
    return index, bm25, filenames

index, bm25, filenames = load_engine()

st.info(f"{len(filenames)} documents indexed.")

query = st.text_input("Search", placeholder="Enter a search query...")

if query:
    results = search(query, index, bm25, filenames)

    if not results:
        st.warning("No results found.")
    else:
        st.markdown(f"**{len(results)} result(s) for:** `{query}`")
        st.divider()

        for r in results:
            with st.container(border=True):
                col1, col2 = st.columns([4, 1])
                with col1:
                    st.markdown(f"#### {r['filename']}")
                    st.caption(r["snippet"] + "...")
                with col2:
                    st.metric("Score", r["score"])