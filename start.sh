#!/bin/bash
echo "Verificando instalação do Gunicorn..."
pip show gunicorn || pip install gunicorn==20.1.0
gunicorn --bind 0.0.0.0:$PORT --workers 4 bot:app
