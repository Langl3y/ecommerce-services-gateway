# -*- coding: utf-8 -*-
import os
import re
import hmac
import hashlib

from datetime import datetime, timezone
from dotenv import load_dotenv

load_dotenv()

base_url = os.getenv("BASE_URL")
auth_url = os.getenv("AUTH_URL")
secret = os.getenv("SECRET")
app_key = os.getenv("APP_KEY")
sign_method = os.getenv("SIGN_METHOD")


# Lấy timestamp cho request
def get_unix_timestamp():
    utc_timenow = datetime.now(timezone.utc)
    full_unix_timestamp = utc_timenow.timestamp()
    split_timestamp = re.split(r"\.", str(full_unix_timestamp))
    timepart = (split_timestamp[1])[:3]

    return split_timestamp[0] + timepart


# Lấy chữ ký cho request
def sign_request(secret, api, parameters):
    sort_dict = sorted(parameters)
    parameters_str = "%s%s" % (api,
                               str().join('%s%s' % (key, parameters[key]) for key in sort_dict))

    h = hmac.new(secret.encode(encoding="utf-8"), parameters_str.encode(encoding="utf-8"), digestmod=hashlib.sha256)

    return h.hexdigest().upper()
