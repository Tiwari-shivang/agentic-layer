import requests
import io
from helper_methods import convert_pdf_to_text, chunk_text_data, get_vector_points, upload_to_qdrant, get_embeddings

def upload_embeddings(pdf_path: str):
    response = requests.get(pdf_path)
    if(response.status_code == 200):
        binary_content = response.content
        stream_data = io.BytesIO(binary_content)
        file_text = convert_pdf_to_text(stream_data)
        chunks = chunk_text_data(file_text, 200)
        points = get_vector_points(chunks)
        upload_to_qdrant(points)
