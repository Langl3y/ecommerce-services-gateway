<p align="center" width="100%">
    <img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png">
    <p style="text-align: center;">
</p>

# FastAPI - Lazada service gateway 

<span style="color:red;font-weight:700;font-size:100px">
    Not tested on Windows.
</span>

## Requirements
- Python 3.10
- FastAPI 1.104.1
- MySQL >= 5.8
- Uvicorn 0.20.0
- SQLAlchemy 2.0.23
- pydantic 2.5.2

## Install Python modules

```shell
./init.sh
```

## Run server for testing

```shell
uvicorn main:app --reload    
```

## Run server (no reload)

```shell
uvicorn main:app
```

## Serve the webapp

```shell
 uvicorn main:app --host 0.0.0.0 --port 8000
```

## Important Note:

This demo will not work if there is no schema for it to connect to. 
Please create a schema in mySQL first, then reconfigure URL_DATABASE so It matches your schema's name.

Also, tables will be automatically created upon creating any object by SQLAlchemy. Be sure not to pre-create any tables inside the schema to avoid conflict.
## APIs Documentation

See: host/docs in your browser for APIs documentation.