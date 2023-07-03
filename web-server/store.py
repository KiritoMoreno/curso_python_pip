import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)
    print(type(r.text))

    # Con el método JSON automaticamente me lo transforma a una lista que python va reconocer y podre hacer iteraciones
    categories = r.json()
    for category in categories:
        print(category['name'])