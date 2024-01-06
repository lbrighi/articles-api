FROM python:3.10-alpine

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

ENV NAME articles
ENV DATABASE_URL sqlite:/app/db.sqlite3

COPY entrypoint.sh /app/entrypoint.sh

RUN chmod +x entrypoint.sh

ENTRYPOINT ["/bin/sh", "/app/entrypoint.sh"]
