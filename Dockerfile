FROM python:3.10.9-alpine3.17

RUN mkdir /app

COPY requirements.txt /app
WORKDIR /app
RUN pip install -r requirements.txt

COPY main.py /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]