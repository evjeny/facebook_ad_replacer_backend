FROM python:3.10.9-alpine3.17

RUN mkdir /app

COPY requirements.txt /app
WORKDIR /app
RUN pip install -r requirements.txt

COPY facebook_ad_replacer_backend /app

CMD ["uvicorn", "app:app", "--host", "0.0.0.0"]