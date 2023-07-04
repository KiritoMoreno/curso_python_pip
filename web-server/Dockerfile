FROM python:3.10

WORKDIR /app


# Copiar los archivos de las dependencias
COPY requirements.txt /app/requirements.txt
# Hace una actualización del gestor de paquetes
RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir -r /app/requirements.txt
# Copiamos todo nuestro codigo (todo)
COPY . /app/

# Este un comando de bash, que va a mantener encendido en servidor uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0","--port", "80"]