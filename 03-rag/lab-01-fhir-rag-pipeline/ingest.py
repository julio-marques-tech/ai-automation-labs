"""Lab 01 - ingest the FHIR corpus: split into chunks, embed them
locally, and store them in a local Chroma vector database."""

import pathlib

import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

CORPUS_DIR = pathlib.Path(__file__).parent / "corpus"
DB_DIR = pathlib.Path(__file__).parent / "chroma_db"
CHUNK_SIZE = 800  # approx characters per chunk


def chunk_text(text: str, source: str) -> list[dict]:
    """Groups paragraphs into chunks of roughly CHUNK_SIZE characters,
    never splitting a paragraph in half."""
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    chunks = []
    current = ""
    for para in paragraphs:
        if current and len(current) + len(para) > CHUNK_SIZE:
            chunks.append(current.strip())
            current = ""
        current += para + "\n\n"
    if current.strip():
        chunks.append(current.strip())
    return [{"text": c, "source": source} for c in chunks]


def main():
    embedding_fn = SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
    client = chromadb.PersistentClient(path=str(DB_DIR))
    collection = client.get_or_create_collection(
        name="fhir_docs", embedding_function=embedding_fn
    )

    all_chunks = []
    for md_file in sorted(CORPUS_DIR.glob("*.md")):
        text = md_file.read_text(encoding="utf-8")
        all_chunks.extend(chunk_text(text, md_file.stem))

    collection.upsert(
        ids=[f"{c['source']}-{i}" for i, c in enumerate(all_chunks)],
        documents=[c["text"] for c in all_chunks],
        metadatas=[{"source": c["source"]} for c in all_chunks],
    )

    print(f"Ingested {len(all_chunks)} chunks from {len(list(CORPUS_DIR.glob('*.md')))} "
          f"documents into '{DB_DIR}'.")


if __name__ == "__main__":
    main()
