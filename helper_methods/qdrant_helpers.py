from pypdf import PdfReader
from config import client, q_client
import uuid
from schemas import kb_req_schema

def get_embeddings(chunk: str):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=chunk
    )
    return response.data[0].embedding

def get_vector_points(request: kb_req_schema, chunks):
    points = []
    for chunk in chunks:
        embedding = get_embeddings(chunk)
        points.append({
            "id": str(uuid.uuid4()),
            "vector": embedding,
            "payload": {
                "tenant_id": request.tenant_id,
                "user_id": request.user_id,
                "file_name": request.file_name,
                "format": request.format,
                "content": chunk,
                "type": "document"
            }
        })
    return points

def chunk_text_data(text: str, chunk_size: int):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:chunk_size+i])
    return chunks

def convert_pdf_to_text(stream_data):
    file_text=""
    reader = PdfReader(stream_data)
    pages = reader.pages
    for page in pages:
        text=page.extract_text()
        if(text):
            file_text += text + "\n"
    return file_text

def search_qdrant(query_emb, tenant_id):
    response = q_client.query_points(
        collection_name="knowledge",
        query=query_emb,
        limit=5,
        query_filter={
            "must": [
                {"key": "tenant_id", "match": {"value": tenant_id}}
            ]
        }
    )
    return response.points

def filter_chunks(embeddings):
    print("embedding found", embeddings)
    return [r for r in embeddings if getattr(r, "score", 0) > 0.5]


def upload_to_qdrant(points):
    q_client.upsert(collection_name="knowledge", points=points)
