import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['A', 'B', 'C']
    values = [200, 34, 120]

    fig, ax = plt.subplots() # Generar la gráfica
    ax.pie(values, labels = labels) # Enviamos los valores y labels
    plt.savefig('pie.png') # Guarda en un archivo
    plt.close()
