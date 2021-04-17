FROM python:alpine

COPY get-bitcoin-data.py requirements.txt /app/

WORKDIR /app

RUN pip install -r requirements.txt

CMD [ "python", "/app/get-bitcoin-data.py" ]
