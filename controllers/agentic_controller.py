from fastapi import APIRouter, Request, BackgroundTasks
from schemas import chat_response, chat_request

router = APIRouter()

@router.post("/chat")
async def chat_agent(request: chat_request) -> chat_response:
    return chat_response(
        response=f"User asked for {request.message}"
    )

@router.post("/webhook/kb-handler")
async def kb_handler(request: Request, background_task: BackgroundTasks):
    req_body = await request.json()