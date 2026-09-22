from typing import List, Optional
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.transaction import Transaction
from app.schemas.transaction import TransactionCreate, TransactionResponse
from app.core.dependencies import get_current_user
from app.models.user import User

router = APIRouter()


@router.post("", response_model=TransactionResponse, status_code=status.HTTP_201_CREATED)
@router.post("/", response_model=TransactionResponse, status_code=status.HTTP_201_CREATED)
def create_transaction(
    transaction_in: TransactionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    db_tx = Transaction(**transaction_in.model_dump())
    db.add(db_tx)
    db.commit()
    db.refresh(db_tx)
    return db_tx


@router.get("/merchant/{merchant_id}", response_model=List[TransactionResponse])
def get_merchant_transactions(
    merchant_id: str,
    status_filter: Optional[str] = Query(None, alias="status"),
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    query = db.query(Transaction).filter(Transaction.merchant_id == merchant_id)
    if status_filter:
        query = query.filter(Transaction.status == status_filter)
    return query.offset(offset).limit(limit).all()