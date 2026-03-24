import uuid
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DATE, TEXT, TIMESTAMP, text as sa_text
from database import BaseClass

class attrition_model(BaseClass):
    __tablename__ = "attritions"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    tenant_id = Column(String(36), ForeignKey("tenants.id"))

    date = Column(DATE, nullable=False)
    department = Column(String(100), nullable=True)
    location = Column(TEXT, nullable=True)

    total_employees = Column(Integer, nullable=False, default=0)
    attrition_count = Column(Integer, nullable=False, default=0)
    attrition_rate = Column(Float, nullable=False, default=0.0)

    created_at = Column(TIMESTAMP(timezone=True), server_default=sa_text('now()'), nullable=False)