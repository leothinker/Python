import chromadb
from google import genai

import chunk

google_client = genai.Client()
EMBEDDING_MODEL = "gemini-embedding-exp-03-07"
LLM_MODEL = "gemini-2.5-flash-preview-05-20"

chromadb_client = chromadb.PersistentClient("./chroma.db")
chromadb_collection = chromadb_client.get_or_create_collection("linghuchong")


def embed(text: str, store: bool) -> list[float]:
    result = google_client.models.embed_content(
        model=EMBEDDING_MODEL,
        contents=text,
        config={"task_type": "RETRIEVAL_DOCUMENT" if store else "RETRIEVAL_QUERY"},
    )

    assert result.embeddings
    assert result.embeddings[0].values
    return result.embeddings[0].values


def create_db() -> None:
    for idx, c in enumerate(chunk.get_chunks()):
        print(f"Process: {c}")
        embedding = embed(c, store=True)
        chromadb_collection.upsert(ids=str(idx), documents=c, embeddings=embedding)


def query_db(question: str) -> list[str]:
    question_embedding = embed(question, store=False)
    result = chromadb_collection.query(query_embeddings=question_embedding, n_results=5)
    assert result["documents"]
    return result["documents"][0]


if __name__ == "__main__":
    question = "令狐冲领悟了什么魔法？"
    # create_db()
    chunks = query_db(question)
    prompt = "Please answer user's question according to context\n"
    prompt += f"Question: {question}\n"
    prompt += "Context:\n"
    for c in chunks:
        prompt += f"{c}\n"
        prompt += "-------------\n"

    result = google_client.models.generate_content(model=LLM_MODEL, contents=prompt)
    print(result)
