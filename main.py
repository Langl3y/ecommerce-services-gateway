import os

from dotenv import load_dotenv
from fastapi import FastAPI
from routers import lazada, tiki
from fastapi.middleware.trustedhost import TrustedHostMiddleware

load_dotenv()

allowed_hosts = os.getenv('ALLOWED_HOSTS')
app = FastAPI()
app.add_middleware(TrustedHostMiddleware, allowed_hosts=allowed_hosts)
app.include_router(lazada.router, prefix="/lazada")
app.include_router(tiki.router, prefix="/tiki")


@app.get("/")
def api_list():
    return {"all_endpoints": [
        "/docs",
        "/lazada/get_token",
        "/lazada/refresh_token",
        "/lazada/order/get",
        "/lazada/orders/get",
        "/lazada/finance/transaction/detail/get",
        "/tiki/get_token"
    ]}


@app.get("/lazada")
def lazada_api_list():
    return {"API": [
        "/get_token",
        "/refresh_token",
        "/order/get",
        "/orders/get",
        "/transaction/detail/get"
    ]}


@app.get("/tiki")
def tiki_api_list():
    return {"API": [
        "/get_token"
    ]}
