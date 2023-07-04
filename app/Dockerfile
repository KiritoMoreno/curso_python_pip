FROM python:3.8

WORKDIR /app
# Copiar los archivos de las dependencias
COPY requirements.txt /app/requirements.txt
# Hace una actualización del gestor de paquetes
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
# Copiamos todo nuestro codigo (todo)
COPY . /app/

# Este un comando de bash, que va a mantener en ejecución constante este contenedor
CMD bash -c "while true; do sleep 1; done"