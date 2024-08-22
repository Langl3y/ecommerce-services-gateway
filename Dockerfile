#
FROM python:3.8
#
WORKDIR /lazada-service-gateway
#
COPY ./requirements.txt /lazada-service-gateway/requirements.txt
#
RUN pip install --no-cache-dir --upgrade -r /lazada-service-gateway/requirements.txt
#
COPY ./.env /lazada-service-gateway/.env
COPY ./common /lazada-service-gateway/common
COPY ./routers /lazada-service-gateway/routers
COPY ./serializers /lazada-service-gateway/serializers
COPY ./services /lazada-service-gateway/services
COPY ./main.py /lazada-service-gateway/main.py
#
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]