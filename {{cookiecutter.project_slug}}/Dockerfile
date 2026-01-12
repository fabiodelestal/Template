# syntax=docker/dockerfile:1

FROM python:3.12-slim

WORKDIR /app

# Copiar requirements
COPY requirements.txt ./

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código
COPY src/ ./src/

# Usuario no-root (seguridad)
RUN useradd --create-home appuser
USER appuser

# Variables de entorno
ENV PYTHONUNBUFFERED=1

# Comando por defecto
CMD ["python", "-m", "{{ cookiecutter.project_slug }}"]
