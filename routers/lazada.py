from fastapi import APIRouter, status
from common.responses import APIResponseCode
from services.lazada import get_laz_token, refresh_laz_token, get_laz_order, get_laz_transaction

router = APIRouter()


@router.get("/get_token", status_code=status.HTTP_200_OK)
async def get_token_handler(code: str):
    response = get_laz_token(code)
    result = {'response': response}
    try:
        if response['access_token']:
            return APIResponseCode.SUCCESS, result
    except Exception as e:
        return APIResponseCode.EXT_API_ERROR, result


@router.get("/refresh_token", status_code=status.HTTP_200_OK)
async def refresh_token_handler(refresh_token: str):
    response = refresh_laz_token(refresh_token)
    result = {'response': response}
    try:
        if response['access_token']:
            return APIResponseCode.SUCCESS, result
    except Exception as e:
        return APIResponseCode.EXT_API_ERROR, result


@router.get("/order/get", status_code=status.HTTP_200_OK)
async def get_sales_order_handler(access_token: str, order_id: str):
    response = get_laz_order(access_token, order_id)
    result = {'response': response}
    try:
        if response['data']:
            return APIResponseCode.SUCCESS, result
    except Exception as e:
        return APIResponseCode.EXT_API_ERROR, result


@router.get("/finance/transaction/details/get", status_code=status.HTTP_200_OK)
async def get_transaction_details_handler(access_token: str, start_time: str, offset: str, end_time: str, limit: str, trans_type: str):
    response = get_laz_transaction(access_token, start_time, offset, end_time, limit, trans_type)
    result = {'response': response}
    try:
        if response['data']:
            return APIResponseCode.SUCCESS, result
    except Exception as e:
        return APIResponseCode.EXT_API_ERROR, result
