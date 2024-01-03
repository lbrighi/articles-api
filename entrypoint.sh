#!/bin/bash

# Aguardar o serviço de banco de dados ficar disponível (se necessário)
# adicione este comando se você perceber que o serviço de banco de dados não está pronto imediatamente
# até mesmo com a flag depends_on no docker-compose.yml
# sleep 10

# Rodar as migrações
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Iniciar o servidor
python manage.py runserver 0.0.0.0:8000
