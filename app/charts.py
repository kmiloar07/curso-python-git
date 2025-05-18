import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt #matplotlib.pyplot es una biblioteca en Python que permite crear gráficos.
#Se importa con el alias plt para facilitar su uso.


def generate_bar_chart2(name, labels, values):
    fig, ax = plt.subplots() #plt.subplots() crea una figura (fig) y un eje (ax). 
    #fig: Representa toda la imagen o gráfico.
    #ax: Representa el área donde se dibuja el gráfico.
    ax.bar(labels, values) #Crea un gráfico de barras con labels (etiquetas) en el eje X y values (valores) en el eje Y.
    plt.savefig(f'./imgs/{name}.png')
    plt.close()

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots() #Crea la figura y el eje donde se dibujará el gráfico.
    ax.pie(values, labels=labels) #Crea un gráfico de pastel con los valores values y sus etiquetas labels.
    ax.axis('equal') #Asegura que el gráfico de pastel sea un círculo perfecto en lugar de una elipse.
    plt.savefig('pie.png')
    plt.close() #Muestra el gráfico en pantalla.

if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    values = [10, 40, 180]
    generate_bar_chart2(labels, values)
    generate_pie_chart(labels, values)


