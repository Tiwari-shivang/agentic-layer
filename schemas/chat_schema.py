from pydantic import BaseModel

class chat_response(BaseModel):
    response: str
    class Config:
        from_attributes=True

class chat_request(BaseModel):
    message: str
    tenant_id: str