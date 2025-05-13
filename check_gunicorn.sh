#!/bin/bash
echo "Verificando instalações..."
which python
which pip
pip show gunicorn || echo "Gunicorn não instalado"
pip list | grep gunicorn || echo "Gunicorn não encontrado"
