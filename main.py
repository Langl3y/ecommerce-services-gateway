import os

from dotenv import load_dotenv
from fastapi import FastAPI
from routers import lazada
from fastapi.middleware.trustedhost import TrustedHostMiddleware

load_dotenv()

allowed_hosts = os.getenv('ALLOWED_HOSTS')
app = FastAPI()
app.add_middleware(TrustedHostMiddleware, allowed_hosts=allowed_hosts)
app.include_router(lazada.router, prefix="/lazada")


@app.get("/")
def root():
    return {"API": [
        "/docs",
        "/lazada/get_token",
        "/lazada/refresh_token",
        "/lazada/order/get",
        "/lazada/orders/get",
        "/lazada/finance/transaction/detail/get"
    ]}
