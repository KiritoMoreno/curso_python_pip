import matplotlib.pyplot as plt
# Creando una gráficas


def generate_bar_chart(labels, values):

  fig, ax = plt.subplots()  # (fig) y (ax) son variables de matplotlib
  ax.bar(labels, values)
  plt.show()


def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)  # aqui debemos indicarle cuales son los labels
  ax.axis('equal')
  plt.show()


if __name__ == '__main__':
  labels = []
  values = []

  generate_bar_char(labels, values)
  #generate_pie_chart(labels, values)
