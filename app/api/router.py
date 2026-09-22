from fastapi import APIRouter
from app.api.v1 import auth, merchants, transactions, webhooks

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
api_router.include_router(merchants.router, prefix="/merchants", tags=["Merchants"])
api_router.include_router(transactions.router, prefix="/transactions", tags=["Transactions"])
api_router.include_router(webhooks.router, prefix="/webhooks", tags=["Webhooks"])