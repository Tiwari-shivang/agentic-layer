from database import BaseClass
from pydantic import BaseModel

class kb_req_schema(BaseModel):
    file_name: str
    tenant_id: str
    format: str
    source: str
    user_id: str
    public_id: str