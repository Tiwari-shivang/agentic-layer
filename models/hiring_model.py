from database import BaseClass
from sqlalchemy import Column, String, ForeignKey, DATE, TEXT, Integer, TIMESTAMP, text as sa_text
from sqlalchemy.orm import relationship
import uuid

class hiring_model(BaseClass):
    __tablename__="hirings"
    id=Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    
    tenant_id=Column(String(36), ForeignKey("tenants.id"))
    Tenant=relationship("tenant_model")

    date=Column(DATE, nullable=False)
    role=Column(TEXT, default="")
    location=Column(TEXT, default="")
    total_opening=Column(Integer, default=0)
    interviews_scheduled=Column(Integer, default=0)
    offers_made=Column(Integer, default=0)
    hires=Column(Integer, default=0)

    created_at=Column(TIMESTAMP(timezone=True), server_default=sa_text('now()'), nullable=False)