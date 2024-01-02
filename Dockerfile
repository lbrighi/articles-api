FROM python:3.10-alpine

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

ENV NAME articles
ENV DATABASE_URL sqlite:////app/db.sqlite3

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
