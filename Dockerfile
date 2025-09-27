# Usa la imagen oficial de Python 3.11.3
FROM python:3.11.3-slim

# Establecer directorio de trabajo
WORKDIR /app

# Instalar dependencias
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiar el código
COPY . /app/
