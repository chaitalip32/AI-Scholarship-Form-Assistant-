from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime

from app.core.database import Base

class Document(Base):
    __tablename__="documents"

    id=Column(Integer, primary_key=True, index=True)

    user_id=Column(Integer, ForeignKey("users.id"))

    document_type=Column(String)

    file_url=Column(Text)

    ocr_text=Column(Text)

    upload_date=Column(DateTime, default=datetime.utcnow)

    user=relationship("User")
