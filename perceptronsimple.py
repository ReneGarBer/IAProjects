import numpy as np
import matplotlib.pyplot as plt
import csv

#crea el dataset a partir de un archivo csv
class DataSet:
    def __init__(self) -> None:
        self.dataset = None
        self.numdatos = None
        pass

    def __str__(self) -> None:
        pass
    
    def setdataset(self,path=""):
        data = np.loadtxt(path,delimiter=',',dtype=float)
        self.dataset = np.array([(tuple(row[:2]), int(row[2])) for row in data], dtype=object)
        self.numdatos = self.dataset.size 


    def printdataset(self):
        print("Datos:")
        for data in self.dataset:
            print(data)

#Clase PerceptronSimple
#Debe recibir un dataset que contiene un par ordenado y el peso

class PerceptronSimple:
    def __init__(self, tasa_aprendizaje=0.05, epocas=100,precision=1.0):        
        self.tasa_aprendizaje = tasa_aprendizaje
        self.epocas = epocas
        self.precision = precision
        self.pesos = None

    def activacion(self, entrada):
        return 1 if entrada >= 0 else -1

    def predecir(self, entradas):
        suma_ponderada = np.dot(entradas, self.pesos[1:]) + self.pesos[0]  # Producto punto + sesgo
        return self.activacion(suma_ponderada)
    
    def entrenar(self, dataset):
        generador = np.random.default_rng()
        self.pesos = generador.random(3)  # genera a pesos
        correctos = 0
        for _ in range(self.epocas):            
            for entrada in dataset.dataset:
                prediccion = self.predecir(entrada[0])
                
                if prediccion == entrada[1]:
                    correctos += 1

                error = entrada[1] - prediccion
                self.pesos[1:] += self.tasa_aprendizaje * error * np.array(entrada[0])
                self.pesos[0] += self.tasa_aprendizaje * error

            precision_actual = correctos /dataset.dataset.size
            
            if precision_actual >= self.precision:
               print("Termino en: ",_," epoca")
               break

    def plot_pares_ordenados(self,pares):
        x = [par[0] for par in pares]
        y = [par[1] for par in pares]

        recta_x = np.linspace(min(x), max(x), 100)               
        recta_y = (-self.pesos[0] * recta_x - perceptron.pesos[1]) / perceptron.pesos[2]
        
        plt.plot(recta_x, recta_y, color='red', label='Recta Separadora')
        plt.scatter(x, y)
        plt.xlabel('Eje X')
        plt.ylabel('Eje Y')
        plt.title('Pares Ordenados en un Plano')
        plt.grid(True)
        plt.legend()
        plt.show()

    def predecirds(self,dataset):
        for entrada in dataset.dataset:
            prediccion = self.predecir(entrada[0])
            print("Entrada: ",entrada[0]," Etiqueta: ",entrada[1],"Prediccion: ",prediccion)
        pares = [par[0] for par in dataset.dataset]
        
        self.plot_pares_ordenados(pares)
        

        



#pedir al usuario el criterio de finalización, número MÁXIMO de épocas, Taza de aprendizaje

# criterioFin = float(input("Criterio de finalización (rango de precision de 0 a 1): "))
# epocas = int(input("Epocas: "))
# tazaAprendizaje = float(input("Taza de aprendizaje: "))

criterioFin = 1
epocas = 50
tazaAprendizaje = 0.05

dataset_trn = DataSet()
dataset_trn.setdataset("iavenv\OR_trn.csv")

perceptron = PerceptronSimple(tazaAprendizaje,epocas,criterioFin)
perceptron.entrenar(dataset_trn)

dataset_tst = DataSet()
dataset_tst.setdataset("iavenv\OR_tst.csv")

perceptron.predecirds(dataset_tst)

dataset_xtrn = DataSet()
dataset_xtrn.setdataset("iavenv\XOR_trn.csv")

perceptron = PerceptronSimple(tazaAprendizaje,epocas,criterioFin)
perceptron.entrenar(dataset_xtrn)

dataset_xtst = DataSet()
dataset_xtst.setdataset("iavenv\XOR_tst.csv")

perceptron.predecirds(dataset_xtst)
