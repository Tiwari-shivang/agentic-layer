from fastapi import APIRouter, Request, BackgroundTasks
from schemas import chat_response, chat_request
from services import upload_embeddings, get_agent_response

router = APIRouter()

@router.post("/chat")
async def chat_agent(request: chat_request) -> chat_response:
    return await get_agent_response(request.message)

@router.post("/webhook/kb-handler")
async def kb_handler(request: Request, background_task: BackgroundTasks):
    req_body = await request.json()
    background_task.add_task(upload_embeddings, req_body.get("secure_url"))
