from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.database import get_db
from app.models.transaction import Transaction

router = APIRouter()

# Schema for incoming webhook payload
class PaymentCallbackPayload(BaseModel):
    transaction_id: str
    provider_tx_id: str
    status: str

@router.post("/payment-callback")
def process_payment_callback(
    payload: PaymentCallbackPayload, 
    db: Session = Depends(get_db)
):
    """Handles async payment callbacks from external providers (e.g., Wave, Orange Money)."""
    # 1. Find the transaction
    transaction = db.query(Transaction).filter(Transaction.id == payload.transaction_id).first()
    
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
        
    # 2. Update transaction details
    transaction.provider_tx_id = payload.provider_tx_id
    transaction.status = payload.status
    
    # 3. Save to database
    db.commit()
    db.refresh(transaction)
    
    return {"message": "Webhook received successfully", "status": transaction.status}