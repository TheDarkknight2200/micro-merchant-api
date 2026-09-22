from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
from datetime import datetime
from app.models.user import UserRole


# Shared properties across user schemas
class UserBase(BaseModel):
    email: EmailStr
    full_name: str
    phone_number: Optional[str] = None
    role: UserRole = UserRole.MERCHANT_OWNER


# Schema for incoming registration requests
class UserCreate(UserBase):
    password: str


# Schema for returning user data (hides hashed_password)
class UserResponse(UserBase):
    id: str
    is_active: bool
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


# Token schema for JWT authentication
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    user_id: Optional[str] = None


class UserLogin(BaseModel):
    email: EmailStr
    password: str