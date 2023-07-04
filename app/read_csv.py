# Leer csv
import csv


def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(
      csvfile, delimiter=','
    )  # delimiter es la separación por columna que tiene el archivo
    header = next(
      reader)  # Tenemos la primer fila de las columnas de forma manual
    data = []
    for row in reader:
      iterable = zip(header, row)  # Hacemos la unión de el (header) y  el (row)

      country_dict = {
        key: value
        for key, value in iterable
      }  # Vamos a generar un Diccionario comprehension a partir del iterable
      data.append(country_dict)
      return data


if __name__ == '__main__':
  data = read_csv('data.csv')
  print(data[0])  # Imprimimos el primero
