
import uuid
from sqlalchemy import Column, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from app.database import Base


class Merchant(Base):
    __tablename__ = "merchants"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), index=True)  # UUID string
    business_name = Column(String, index=True, nullable=False)
    tax_id = Column(String, unique=True, nullable=True)  # e.g., NINEA in Senegal
    currency = Column(String, default="XOF", nullable=False)  # Defaulting to West African CFA
    owner_id = Column(String, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    owner = relationship("User", back_populates="merchants")
    transactions = relationship("Transaction", back_populates="merchant", cascade="all, delete-orphan")