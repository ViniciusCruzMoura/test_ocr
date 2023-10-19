FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

RUN cd / \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY ./main.py ./main.py