from fastapi import APIRouter, status
from typing import Optional

from services.tiki import get_tiki_token
from common.responses import APIResponseCode

router = APIRouter()


@router.post("/get_token", status_code=status.HTTP_200_OK)
async def get_token_handler():
    response = get_tiki_token()
    result = {'response': response}
    try:
        if response['access_token']:
            return APIResponseCode.SUCCESS, result
    except Exception as e:
        return APIResponseCode.EXT_API_ERROR, result
