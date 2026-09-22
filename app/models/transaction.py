import uuid
import enum
from sqlalchemy import Column, String, Numeric, Enum, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from app.database import Base


class PaymentProvider(str, enum.Enum):
    WAVE = "wave"
    ORANGE_MONEY = "orange_money"
    CASH = "cash"
    CARD = "card"


class TransactionStatus(str, enum.Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), index=True)  # UUID string
    merchant_id = Column(String, ForeignKey("merchants.id", ondelete="CASCADE"), nullable=False)
    amount = Column(Numeric(precision=12, scale=2), nullable=False)  # Decimal precision for money
    currency = Column(String, default="XOF", nullable=False)
    provider = Column(Enum(PaymentProvider), nullable=False)
    status = Column(Enum(TransactionStatus), default=TransactionStatus.PENDING, nullable=False)
    provider_tx_id = Column(String, unique=True, index=True, nullable=True)  # External webhook reference ID
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    merchant = relationship("Merchant", back_populates="transactions")