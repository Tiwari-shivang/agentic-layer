from database import BaseClass
from sqlalchemy import Column, String, ForeignKey, TIMESTAMP, text as sa_text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB
import uuid

class theme_model(BaseClass):
    __tablename__="user_preferences"
    id=Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String(36), ForeignKey("users.id"))
    User = relationship("user_model")
    dashboard_layout = Column(JSONB, nullable=True)
    created_at = Column(TIMESTAMP, server_default=sa_text("now()"), nullable=True)
