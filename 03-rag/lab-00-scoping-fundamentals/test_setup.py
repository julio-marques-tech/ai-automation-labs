"""Smoke test: confirms the local embedding model downloads and runs,
and that semantically similar sentences end up with similar embeddings
(closer cosine similarity) than unrelated ones."""

from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "The Patient resource represents a person receiving healthcare services.",
    "A Patient resource models an individual who is a recipient of care.",
    "The stock market closed higher today after strong earnings reports.",
]

embeddings = model.encode(sentences)

sim_related = util.cos_sim(embeddings[0], embeddings[1]).item()
sim_unrelated = util.cos_sim(embeddings[0], embeddings[2]).item()

print(f"Similarity between related sentences (both about Patient resource): {sim_related:.3f}")
print(f"Similarity between unrelated sentences (Patient vs. stock market): {sim_unrelated:.3f}")
print()
print("Expected: the first number should be clearly higher than the second.")
