from fastapi import APIRouter
from schemas import chat_response, chat_request

router = APIRouter()

@router.post("/chat")
async def chat_agent(request: chat_request) -> chat_response:
    return chat_response(
        response=f"User asked for {request.message}"
    )
