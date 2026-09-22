import enum
import uuid
from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship
from app.database import Base


class UserRole(str, enum.Enum):
    MERCHANT_OWNER = "merchant_owner"
    CASHIER = "cashier"
    ADMIN = "admin"


class User(Base):
    __tablename__ = "users"

    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        index=True,
    )
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    phone_number = Column(String, index=True, nullable=False)
    role = Column(String, nullable=False, default=UserRole.MERCHANT_OWNER.value)
    is_active = Column(Boolean, default=True)

    merchants = relationship("Merchant", back_populates="owner")