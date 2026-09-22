from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.merchant import Merchant
from app.schemas.merchant import MerchantCreate, MerchantResponse
from app.core.dependencies import get_current_user
from app.models.user import User

router = APIRouter()


@router.post("", response_model=MerchantResponse, status_code=status.HTTP_201_CREATED)
@router.post("/", response_model=MerchantResponse, status_code=status.HTTP_201_CREATED)
def create_merchant(
    merchant_in: MerchantCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    merchant = Merchant(
        business_name=merchant_in.business_name,
        tax_id=merchant_in.tax_id,
        currency=merchant_in.currency,
        owner_id=current_user.id,
    )
    db.add(merchant)
    db.commit()
    db.refresh(merchant)
    return merchant