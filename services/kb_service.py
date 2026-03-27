import requests
import io
from schemas import kb_req_schema
from helper_methods import convert_pdf_to_text, chunk_text_data, get_vector_points, upload_to_qdrant, get_embeddings

def upload_embeddings(request: kb_req_schema):
    response = requests.get(request.source)
    if(response.status_code == 200):
        try:
            binary_content = response.content
            stream_data = io.BytesIO(binary_content)
            file_text = convert_pdf_to_text(stream_data)
            chunks = chunk_text_data(file_text, 200)
            points = get_vector_points(request, chunks)
            upload_to_qdrant(points)
            return True
        except Exception as e:
            print(e)
            return False

