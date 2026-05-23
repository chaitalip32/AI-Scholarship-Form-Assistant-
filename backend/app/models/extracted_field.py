from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.core.database import Base


class ExtractedField(Base):
    __tablename__ = "extracted_fields"

    id = Column(Integer, primary_key=True, index=True)

    application_id = Column(Integer, ForeignKey("applications.id"))

    field_name = Column(String)

    field_value = Column(String)

    confidence_score = Column(Float)

    application = relationship("Application")