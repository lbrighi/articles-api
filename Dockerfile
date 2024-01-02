# Use a imagem base do Python
FROM python:3.10-alpine

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

ENV NAME articles
ENV DATABASE_URL sqlite:/app/db.sqlite3

# Copiar o script de entrada para o contêiner
COPY entrypoint.sh /app/entrypoint.sh

# Tornar o script de entrada executável
RUN chmod +x entrypoint.sh

# Definir o comando de entrada como o script
ENTRYPOINT ["/bin/sh", "/app/entrypoint.sh"]
