import matplotlib.pyplot as plt
# Creando una gráficas


def generate_bar_chart(name,labels,values):

  fig, ax = plt.subplots()  # (fig) y (ax) son variables de matplotlib
  ax.bar(labels, values)
  plt.savefig(f'./imgs/{name}.png') # Guarda en un archivo
  plt.close()


def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)  # aqui debemos indicarle cuales son los labels
  ax.axis('equal')
  plt.savefig('pie.png') # Guarda en un archivo
  plt.close()

if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [10, 40, 600]

  #generate_bar_char(labels, values)
  generate_pie_chart(labels, values)
