# -*- coding: utf-8 -*-
import requests
import urllib3

from common.utils import *

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# Lấy access token từ Lazada
def get_laz_token(code):
    api = '/auth/token/create'
    url = auth_url + api

    params = {
        "app_key": app_key,
        "timestamp": get_unix_timestamp(),
        "sign_method": sign_method,
        "code": code,
        "secret": secret
    }
    sign = sign_request(secret, api, params)
    params.update({"sign": sign})
    response = requests.get(url, params=params)

    return response.json()


def refresh_laz_token(refresh_token):
    api = '/auth/token/refresh'
    url = auth_url + api

    params = {
        "refresh_token": refresh_token,
        "app_key": app_key,
        "timestamp": get_unix_timestamp(),
        "sign_method": sign_method,
        "secret": secret
    }
    sign = sign_request(secret, api, params)
    params.update({"sign": sign})
    response = requests.get(url, params=params)

    return response.json()


def get_laz_order(access_token, order_id):
    api = '/order/get'
    url = base_url + api

    params = {
        "order_id": order_id,
        "app_key": app_key,
        "access_token": access_token,
        "timestamp": get_unix_timestamp(),
        "sign_method": sign_method,
    }
    sign = sign_request(secret, api, params)
    params.update({"sign": sign})
    response = requests.get(url, params=params)

    return response.json()


def get_laz_transaction(access_token, start_time, offset, end_time, limit, trans_type):
    api = '/finance/transaction/detail/get'
    url = base_url + api

    params = {
        "start_time": start_time,
        "offset": offset,
        "end_time": end_time,
        "limit": limit,
        "trans_type": trans_type,
        "app_key": app_key,
        "access_token": access_token,
        "timestamp": get_unix_timestamp(),
        "sign_method": sign_method,
    }
    sign = sign_request(secret, api, params)
    params.update({"sign": sign})
    response = requests.get(url, params=params)

    return response.json()
