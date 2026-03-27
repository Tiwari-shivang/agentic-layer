from pydantic import BaseModel

class success_message(BaseModel):
    is_success:bool
    message:str
    class Config:
        from_attributes=True