import os
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download("stopwords", quiet=True)

stemmer = PorterStemmer()
stop_words = set(stopwords.words("english"))


def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    tokens = text.split()
    tokens = [stemmer.stem(t) for t in tokens if t not in stop_words]
    return tokens


def load_documents(docs_dir):
    docs = {}
    for filename in os.listdir(docs_dir):
        if filename.endswith(".txt"):
            filepath = os.path.join(docs_dir, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                docs[filename] = f.read()
    return docs


def build_index(docs):
    index = {}
    for name, content in docs.items():
        index[name] = {
            "raw": content,
            "tokens": preprocess(content)
        }
    return index