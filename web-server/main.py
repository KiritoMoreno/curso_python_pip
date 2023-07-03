import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
# Instancia
app = FastAPI()


@app.get('/') # Decorador- La ruta donde vamos a ingresar
def get_list():
    return [1,2,3]


@app.get('/contact',response_class=HTMLResponse) # Decorador- La ruta donde vamos a ingresar
def get_list():
    return'''
    <h1>Hola soy una pagina</h1>
    <p>Soy un parrafo</p>
    '''
#  uvicorn main:app --reload (comando para usar en la terminal)
def run():
    store.get_categories()

if __name__ == "__main__":
    run()