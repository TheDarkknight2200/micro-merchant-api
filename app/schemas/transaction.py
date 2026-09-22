from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from datetime import datetime
from decimal import Decimal
from app.models.transaction import PaymentProvider, TransactionStatus


class TransactionBase(BaseModel):
    merchant_id: str
    amount: Decimal = Field(..., gt=0, description="Amount must be greater than zero")
    currency: str = "XOF"
    provider: PaymentProvider


# Schema for creating/initiating a payment
class TransactionCreate(TransactionBase):
    pass


# Schema for external payment webhooks (e.g., Wave or Orange Money notifications)
class WebhookPayload(BaseModel):
    transaction_id: str
    provider_tx_id: str
    status: TransactionStatus


# Schema for returning transaction details
class TransactionResponse(TransactionBase):
    id: str
    status: TransactionStatus
    provider_tx_id: Optional[str] = None
    created_at: Optional[datetime] = None  # Make this Optional

    model_config = ConfigDict(from_attributes=True)