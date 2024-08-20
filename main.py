from fastapi import FastAPI
from routers import lazada


app = FastAPI()
app.include_router(lazada.router, prefix="/lazada")


@app.get("/")
def root():
    return {"API": [
        "/docs",
        "/lazada/get_token",
        "/lazada/refresh_token",
        "/lazada/order/get",
    ]}
