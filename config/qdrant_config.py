from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
import os

q_client = QdrantClient(os.getenv("QDRANT_URL"))

q_client.create_collection("knowledge", vectors_config=VectorParams(
    size=1536,
    distance=Distance.COSINE
))