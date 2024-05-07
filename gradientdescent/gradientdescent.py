import math
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import tkinter as tk

def loss_function(x1, x2):
     return (x1 - 2)**2 + (x2 - 3)**2

def function(x1, x2):
    e = 2.71828
    a = x1*x1
    b = 3*(x2*x2)
    i = e**-(a+b)
    return 10 - i

def partial_derivative_respect_to_x1(x1, x2):
     e = 2.71828
     a = x1*x1
     b = 3*(x2*x2)
     i = e**-(a+b)
     return (-2*x1) * i

def partial_derivative_respect_to_x2(x1, x2):
     e = 2.71828
     a = x1*x1
     b = 3*x2*x2
     i = e**-(a+b)
     return (-6*x2) * i

def gradient_descent(learning_rate, x1, x2, iterations):
    x = []
    y = []
    for _ in range(iterations):
        grdx1 = partial_derivative_respect_to_x1(x1, x2)
        grdx2 = partial_derivative_respect_to_x2(x1, x2)
        x1 -= learning_rate * grdx1
        x2 -= learning_rate * grdx2
        x.append(x1)
        y.append(x2)
    return [x1, x2],x,y

def obtener_numero():
    plt.close()
    initial_x1 = random.uniform(0.0, 10.0)
    initial_x2 = random.uniform(0.0, 10.0)
    learning_rate = float(entrada_numero.get())
    iterations = 100
    resultados,x,y = gradient_descent(learning_rate,initial_x1,initial_x2,iterations)

    # Create data for 3D graph
    x3d = np.linspace(-5, 5, 100)
    y3d = np.linspace(-5, 5, 100)
    x3d, y3d = np.meshgrid(x3d, y3d)
    z3d = function(x3d, y3d)

    # Create a 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x3d, y3d, z3d, cmap='cool')


    # Add labels and title for 3D plot
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('f(x1,x2) = 10 - e**-(x1**2+3*x2**2)')

    # Create a 2D scatter plot
    plt.figure()
    plt.scatter(x, y)

    # Add labels and title for 2D scatter plot
    plt.xlabel('x1')
    plt.ylabel('x2')
    title = "learning_rate = {}\n x1 = {}, x2= {}".format(learning_rate,resultados[0],resultados[1])
    plt.title(title)

    # Show both plots
    plt.show()

# Crear la ventana
ventana = tk.Tk()
ventana.title("Interfaz Gráfica")

# Crear un cuadro de entrada (Entry) para que el usuario introduzca el número
entrada_numero = tk.Entry(ventana)
entrada_numero.pack()

# Crear un botón para que el usuario pueda presionarlo
boton = tk.Button(ventana, text="Tasa de aprendizaje", command=obtener_numero)
boton.pack()

# Ejecutar el bucle de eventos de la interfaz gráfica
ventana.mainloop()