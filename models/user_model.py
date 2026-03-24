from database import BaseClass
from sqlalchemy import Column, String, ForeignKey, TIMESTAMP, text as sa_text
from sqlalchemy.orm import relationship
import uuid

class user_model(BaseClass):
    __tablename__="users"
    id=Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    email=Column(String(100), unique=True, nullable=False)
    name=Column(String(100))
    password_hash=Column(String(500))
    
    tenant_id=Column(String(36), ForeignKey("tenants.id"))
    Tenant=relationship("tenant_model")

    role_id=Column(String(36), ForeignKey("roles.id"))
    Role=relationship("role_model")

    created_at=Column(TIMESTAMP(timezone=True), server_default=sa_text('now()'), nullable=False)