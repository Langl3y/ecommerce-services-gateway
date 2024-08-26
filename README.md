<p align="center" width="100%">
    <img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png">
    <p style="text-align: center;">
</p>

# FastAPI - Lazada service gateway 

<span style="color:red;font-weight:700;font-size:50px">
    Tested on Windows
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

## Env

Create `.env` file

```shell
cp .env.sample .env
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
 uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## Docker
#### Containerize

```shell
 docker build -t lazada-gateway .
```

#### Docker run

```shell
docker run -d --name lazada-gateway -p 8000:8000 lazada-gateway                        
```

## Important Note:


## APIs Documentation

See: host/docs in your browser for APIs documentation.