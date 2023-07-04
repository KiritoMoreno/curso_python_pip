import utils
import read_csv
import charts
import os
import pandas as pd

def run():
  # Ruta del directorio de imágenes
  directory = './imgs'

  # Comprobar si el directorio existe, si no, crearlo
  if not os.path.exists(directory):
    os.makedirs(directory)

  df = pd.read_csv('data.csv') # nos ahorramos el metodo 
  df = df[df['Continent'] == 'Sout America']
  # Función en pandas que nos entrega directamente los valores
  countries = df['Country/Territory'].values
  percentages = df['World Population Percentage'].values

  charts.generate_pie_chart(countries, percentages)

  data = read_csv.read_csv('data.csv')
  
  country = input('Type Country : ')
  print(country)

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    print(country)
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'],labels, values)


if __name__ == '__main__':
  run()
