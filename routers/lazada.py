from fastapi import APIRouter, status
from typing import Optional

from common.responses import APIResponseCode
from serializers.lazada import GetTokenLazada, RefreshTokenLazada, GetOrderLazada, GetOrdersLazada, GetTransactionLazada
from services.lazada import get_laz_token, refresh_laz_token, get_laz_order, get_laz_orders, get_laz_transaction

router = APIRouter()


@router.post("/get_token", status_code=status.HTTP_200_OK)
async def get_token_handler(data_body: Optional[GetTokenLazada]):
    response = get_laz_token(data_body)
    result = {'response': response}
    try:
        if response['access_token']:
            return APIResponseCode.SUCCESS, result
    except Exception as e:
        return APIResponseCode.EXT_API_ERROR, result


@router.post("/refresh_token", status_code=status.HTTP_200_OK)
async def refresh_token_handler(data_body: Optional[RefreshTokenLazada]):
    response = refresh_laz_token(data_body)
    result = {'response': response}
    try:
        if response['access_token']:
            return APIResponseCode.SUCCESS, result
    except Exception as e:
        return APIResponseCode.EXT_API_ERROR, result


@router.post("/order/get", status_code=status.HTTP_200_OK)
async def get_sales_order_handler(data_body: Optional[GetOrderLazada]):
    response = get_laz_order(data_body)
    result = {'response': response}
    try:
        if response['data']:
            return APIResponseCode.SUCCESS, result
    except Exception as e:
        return APIResponseCode.EXT_API_ERROR, result


@router.post("/orders/get", status_code=status.HTTP_200_OK)
async def get_sales_order_handler(data_body: Optional[GetOrdersLazada]):
    response = get_laz_orders(data_body)
    result = {'response': response}
    try:
        if response['data']:
            return APIResponseCode.SUCCESS, result
    except Exception as e:
        return APIResponseCode.EXT_API_ERROR, result


@router.post("/finance/transaction/details/get", status_code=status.HTTP_200_OK)
async def get_transaction_details_handler(data_body: Optional[GetTransactionLazada]):
    response = get_laz_transaction(data_body)
    result = {'response': response}
    try:
        if response['data']:
            return APIResponseCode.SUCCESS, result
    except Exception as e:
        return APIResponseCode.EXT_API_ERROR, result
