from pydantic import BaseModel
from typing import Optional


class GetTokenLazada(BaseModel):
    code: str


class RefreshTokenLazada(BaseModel):
    refresh_token: str


class GetOrderLazada(BaseModel):
    access_token: str
    order_id: str


class GetTransactionLazada(BaseModel):
    access_token: str
    start_time: str
    end_time: str
    offset: Optional[str] = None
    trans_type: Optional[str] = None
    trade_order_id: Optional[str] = None
    limit: Optional[str] = None
    trade_order_line_id: Optional[str] = None


class GetOrdersLazada(BaseModel):
    access_token: str
    update_before: Optional[str] = None
    sort_direction: Optional[str] = None
    offset: Optional[int] = None
    limit: Optional[int] = None
    update_after: Optional[str] = None
    sort_by: Optional[str] = None
    created_before: Optional[str] = None
    created_after: Optional[str] = None
    status: Optional[str] = None
