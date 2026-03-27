from fastapi import APIRouter
from schemas import chat_response, chat_request, kb_req_schema, success_message
from services import upload_embeddings, get_agent_response

router = APIRouter()

@router.post("/chat")
async def chat_agent(request: chat_request) -> chat_response:
    return await get_agent_response(request.message, request.tenant_id)

@router.post("/kb-handler")
async def kb_handler(request: kb_req_schema):
    response = upload_embeddings(request=request)
    if response:
        return success_message(is_success=True, message="Kb ingested")
    return success_message(is_success=False, message="Error kb ingest")
