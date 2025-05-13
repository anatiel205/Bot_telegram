#!/bin/bash
# Verifica instalações
./check_gunicorn.sh

# Inicia o serviço
exec gunicorn --bind 0.0.0.0:$PORT --timeout 120 --workers 4 bot:app
