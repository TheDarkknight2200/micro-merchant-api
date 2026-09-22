from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime


class MerchantBase(BaseModel):
    business_name: str
    tax_id: Optional[str] = None
    currency: str = "XOF"


# Schema for creating a merchant
class MerchantCreate(MerchantBase):
    pass


# Schema for returning merchant details
class MerchantResponse(MerchantBase):
    id: str
    owner_id: str
    created_at: Optional[datetime] = None  # Make this Optional

    model_config = ConfigDict(from_attributes=True)