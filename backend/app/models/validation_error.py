from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.core.database import Base


class ValidationError(Base):
    __tablename__ = "validation_errors"

    id = Column(Integer, primary_key=True, index=True)

    application_id = Column(Integer, ForeignKey("applications.id"))

    error_message = Column(String)

    severity = Column(String)

    application = relationship("Application")