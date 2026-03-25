import requests
import io
from pypdf import PdfReader
from config import client, q_client
import uuid

def get_embeddings(chunk: str):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=chunk
    )
    return response.data[0].embedding

def get_vector_points(chunks):
    points = []
    for chunk in chunks:
        embedding = get_embeddings(chunk)
        points.append({
            "id": str(uuid.uuid4()),
            "vector": embedding,
            "payload": {
                "tenant_id": 101,
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

def upload_to_qdrant(points):
    q_client.upsert(collection_name="knowledge", points=points)

def upload_embeddings(pdf_path: str):
    response = requests.get(pdf_path)
    if(response.status_code == 200):
        binary_content = response.content
        stream_data = io.BytesIO(binary_content)
        file_text = convert_pdf_to_text(stream_data)
        chunks = chunk_text_data(file_text, 200)
        points = get_vector_points(chunks)
        upload_to_qdrant(points)



