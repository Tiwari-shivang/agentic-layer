from database import BaseClass
from sqlalchemy import String, Column, TIMESTAMP, TEXT, text as sa_text
import uuid
class tenant_model(BaseClass):
    __tablename__="tenants"
    id=Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name=Column(String(100), unique=True, nullable=False)
    industry=Column(String(100), nullable=False)
    web_url=Column(TEXT, nullable=True)
    description=Column(TEXT, nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=sa_text('now()') 
    )