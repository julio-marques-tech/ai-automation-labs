"""Lab 01 - query the FHIR RAG pipeline: retrieve the most relevant
chunks from Chroma, then ask Claude to answer using only that context,
citing the source document for every claim."""

import asyncio
import pathlib
import sys

import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

from claude_agent_sdk import ClaudeAgentOptions, ClaudeSDKClient

DB_DIR = pathlib.Path(__file__).parent / "chroma_db"
TOP_K = 3


def retrieve(question: str) -> list[dict]:
    embedding_fn = SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
    client = chromadb.PersistentClient(path=str(DB_DIR))
    collection = client.get_collection(name="fhir_docs", embedding_function=embedding_fn)

    results = collection.query(query_texts=[question], n_results=TOP_K)
    chunks = []
    for doc, meta, dist in zip(
        results["documents"][0], results["metadatas"][0], results["distances"][0]
    ):
        chunks.append({"text": doc, "source": meta["source"], "distance": dist})
    return chunks


async def ask(question: str, chunks: list[dict]):
    context = "\n\n---\n\n".join(
        f"[Source: {c['source']}]\n{c['text']}" for c in chunks
    )
    prompt = (
        "Answer the question using ONLY the context below. Cite the "
        "source (in brackets, e.g. [Source: patient]) for every claim. "
        "If the context doesn't contain the answer, say so explicitly "
        "instead of guessing.\n\n"
        f"CONTEXT:\n{context}\n\nQUESTION: {question}"
    )

    options = ClaudeAgentOptions()
    async with ClaudeSDKClient(options=options) as client:
        await client.query(prompt)
        async for message in client.receive_response():
            print(message)


def main():
    question = (
        sys.argv[1] if len(sys.argv) > 1
        else "What is the cardinality of Patient.gender, and what are its allowed values?"
    )
    print(f"Question: {question}\n")

    chunks = retrieve(question)
    print("Retrieved chunks:")
    for c in chunks:
        print(f"  - {c['source']} (distance={c['distance']:.3f})")
    print()

    asyncio.run(ask(question, chunks))


if __name__ == "__main__":
    main()
