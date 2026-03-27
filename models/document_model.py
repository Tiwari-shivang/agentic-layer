from database import BaseClass
from sqlalchemy import String, TEXT, Column, ForeignKey, TIMESTAMP, text as sa_text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
import uuid

class document_model(BaseClass):
    __tablename__="documents"
    id=Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    
    tenant_id=Column(String(36), ForeignKey('tenants.id'))
    Tenant=relationship("tenant_model")

    file_type=Column(String(50), nullable=False)
    file_name=Column(String(100), nullable=False)
    content=Column(TEXT, nullable=False)
    meta_data=Column(JSONB, nullable=False)
    created_at=Column(TIMESTAMP, server_default=sa_text('now()'))