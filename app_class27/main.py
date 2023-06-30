import utils
import read_csv
import charts
import os


def run():
  data = read_csv.read_csv('data.csv')
  
  data = list(filter(lambda item: item["Continent"] == "South America", data))

  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x["World Population Percent"], data))
  # Ruta del directorio de imágenes
  directory = './imgs'

  # Comprobar si el directorio existe, si no, crearlo
  if not os.path.exists(directory):
    os.makedirs(directory)
  charts.generate_pie_chart(countries, percentages)
  
  
  
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
