from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm  import relationship
from datetime import datetime

from app.core.database import Base

class Application(Base):
    __tablename__="applications"

    id=Column(Integer, primary_key=True, index=True)

    user_id=Column(Integer, ForeignKey("users.id"))

    scholarship_name= Column(String)

    status=Column(String, default="pending")

    generated_pdf_url=Column(String, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)

    user=relationship("User")