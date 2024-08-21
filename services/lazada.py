# -*- coding: utf-8 -*-
import requests
import urllib3

from common.utils import *

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_laz_token(data_body):
    api = '/auth/token/create'
    url = auth_url + api

    params = {
        "app_key": app_key,
        "timestamp": get_unix_timestamp(),
        "sign_method": sign_method,
        "secret": secret
    }
    params.update(data_body.dict())

    sign = sign_request(secret, api, params)
    params.update({"sign": sign})
    response = requests.get(url, params=params)

    return response.json()


def refresh_laz_token(data_body):
    api = '/auth/token/refresh'
    url = auth_url + api

    params = {
        "app_key": app_key,
        "timestamp": get_unix_timestamp(),
        "sign_method": sign_method,
        "secret": secret
    }
    params.update(data_body.dict())

    sign = sign_request(secret, api, params)
    params.update({"sign": sign})
    response = requests.get(url, params=params)

    return response.json()


def get_laz_order(data_body):
    api = '/order/get'
    url = base_url + api

    params = {
        "app_key": app_key,
        "timestamp": get_unix_timestamp(),
        "sign_method": sign_method,
    }
    params.update(data_body.dict())

    sign = sign_request(secret, api, params)
    params.update({"sign": sign})
    response = requests.get(url, params=params)

    return response.json()


def get_laz_orders(data_body):
    api = '/orders/get'
    url = base_url + api

    params = {
        "app_key": app_key,
        "timestamp": get_unix_timestamp(),
        "sign_method": sign_method,
    }
    for k, v in data_body.dict().items():
        if v is not None:
            params.update({k: v})

    sign = sign_request(secret, api, params)
    params.update({"sign": sign})
    response = requests.get(url, params=params)

    return response.json()


def get_laz_transaction(data_body):
    api = '/finance/transaction/details/get'
    url = base_url + api

    params = {
        "app_key": app_key,
        "timestamp": get_unix_timestamp(),
        "sign_method": sign_method,
    }
    for k, v in data_body.dict().items():
        if v is not None:
            params.update({k: v})

    sign = sign_request(secret, api, params)
    params.update({"sign": sign})
    response = requests.get(url, params=params)

    return response.json()
