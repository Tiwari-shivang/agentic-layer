from database import BaseClass
from sqlalchemy import Column, String
import uuid
class role_model(BaseClass):
    __tablename__="roles"
    id=Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name=Column(String(50), nullable=False)