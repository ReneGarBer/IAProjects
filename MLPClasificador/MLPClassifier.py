import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split as tts, LeaveOneOut as loo, KFold as kf
from sklearn.neural_network import MLPClassifier as mlp
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import warnings

def button_clicked():
    fun = {'Sigmoid': 'logistic', 'ReLU': 'relu',
           'Hyperbolic tangent': 'tanh', 'Identity': 'identity'}.get(dropdown_var.get(), 'logistic')

    solver = {'LBFGS': 'lbfgs', 'Stochastic Gradient Descent': 'sgd',
           'Adam': 'adam'}.get(dropdown1_var.get(), 'sgd')
    dataset = text_entry.get()

    max_iter = int(iter_entry.get())
    n_hidden_layers = int(layers_entry.get())  # Number of hidden layers
    neurons_per_layer = int(neruon_entry.get())  # Number of neurons per hidden layer
    hidden_layer_sizes = tuple([neurons_per_layer] * n_hidden_layers)

    data = pd.read_csv(dataset)
    xy = data.iloc[:, :-1]
    label = data.iloc[:, -1]
    x_train, x_test, y_train, y_test = tts(xy,label, test_size=0.2, random_state=42)

    # Crear y entrenar la red neuronal
    modelo = mlp(hidden_layer_sizes=hidden_layer_sizes, activation=fun,solver=solver, random_state=1, max_iter=max_iter)
    #modelo = mlp()
    modelo.fit(x_train,y_train)
    y_predict=modelo.predict(x_test)
    # print(y_predict)
    # print(y_test.values)

    xy_test = x_test.values
    lbl_test = y_test.values
    # lbl_predict = y_predict.values
    #Graficar
    plt.subplot(1,2,1)
    plt.scatter(xy_test[:, 0], xy_test[:, 1], c=lbl_test, cmap=plt.cm.coolwarm, edgecolors='k')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Valores reales')

    plt.subplot(1,2,2)
    plt.scatter(xy_test[:, 0], xy_test[:, 1], c=y_predict, cmap=plt.cm.coolwarm, edgecolors='k')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Predicciones')


    
    # plt.scatter(xy[:, 0], xy[:, 1], c=label, cmap=plt.cm.coolwarm, edgecolors='k')
    # plt.xlabel('x')
    # plt.ylabel('y')
    # plt.title(dataset)
    plt.show()

def mostrar_dataset():
    dataset = text_entry.get()
    data = pd.read_csv(dataset)
    xy = data.iloc[:, :-1].values
    label = data.iloc[:, -1].values
    plt.scatter(xy[:, 0], xy[:, 1], c=label, cmap=plt.cm.coolwarm, edgecolors='k')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(dataset)
    plt.show()

# Create main window
root = tk.Tk()
root.title("Práctca 1, ejercicio 3")

# Number field
text_label = ttk.Label(root, text="Dataset:")
text_label.grid(row=0, column=0, padx=10, pady=5)
text_entry = ttk.Entry(root)
text_entry.grid(row=0, column=1, padx=10, pady=5)

# Number field
layers_label = ttk.Label(root, text="Capas internas:")
layers_label.grid(row=1, column=0, padx=10, pady=5)
layers_entry = ttk.Entry(root)
layers_entry.grid(row=1, column=1, padx=10, pady=5)

# Number field
neruon_label = ttk.Label(root, text="Neuronas por capa:")
neruon_label.grid(row=2, column=0, padx=10, pady=5)
neruon_entry = ttk.Entry(root)
neruon_entry.grid(row=2, column=1, padx=10, pady=5)

# Number field
iter_label = ttk.Label(root, text="Iteraciones:")
iter_label.grid(row=3, column=0, padx=10, pady=5)
iter_entry = ttk.Entry(root)
iter_entry.grid(row=3, column=1, padx=10, pady=5)

# Dropdown menu
dropdown_label = ttk.Label(root, text="Función de activación:")
dropdown_label.grid(row=4, column=0, padx=10, pady=5)
options = ["Sigmoid", "ReLU", "Hyperbolic tangent","Identity"]
dropdown_var = tk.StringVar(root)
dropdown = ttk.Combobox(root, textvariable=dropdown_var, values=options)
dropdown.grid(row=4, column=1, padx=10, pady=5)
dropdown.current(0)  # Set default value

# Dropdown menu
solver_label = ttk.Label(root, text="Solver:")
solver_label.grid(row=5, column=0, padx=10, pady=5)
options1 = ["LBFGS", "Stochastic Gradient Descent", "Adam"]
dropdown1_var = tk.StringVar(root)
dropdown1 = ttk.Combobox(root, textvariable=dropdown1_var, values=options1)
dropdown1.grid(row=5, column=1, padx=10, pady=5)
dropdown1.current(0)  # Set default value

# Button
button = ttk.Button(root, text="analizar", command=button_clicked)
button.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

# Button
button1 = ttk.Button(root, text="Mostrar Dataset", command=mostrar_dataset)
button1.grid(row=6, column=1, columnspan=2, padx=10, pady=5)

# Start GUI
root.mainloop()
