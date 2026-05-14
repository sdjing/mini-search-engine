from rank_bm25 import BM25Okapi
from indexer import preprocess


def build_bm25(index):
    corpus = [data["tokens"] for data in index.values()]
    filenames = list(index.keys())
    bm25 = BM25Okapi(corpus)
    return bm25, filenames


def search(query, index, bm25, filenames, top_n=5):
    tokens = preprocess(query)
    scores = bm25.get_scores(tokens)

    ranked = sorted(
        zip(filenames, scores),
        key=lambda x: x[1],
        reverse=True
    )[:top_n]

    results = []
    for filename, score in ranked:
        if score > 0:
            raw = index[filename]["raw"]
            snippet = raw[:300].replace("\n", " ")
            results.append({
                "filename": filename,
                "score": round(score, 4),
                "snippet": snippet
            })

    return results