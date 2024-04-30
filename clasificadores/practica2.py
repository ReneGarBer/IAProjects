import metricas as mt
import pandas as pd

from sklearn.neighbors import KNeighborsClassifier, kneighbors_graph
from sklearn.linear_model import LogisticRegression 
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split 
from sklearn.svm import OneClassSVM 
from sklearn.metrics import accuracy_score, classification_report

#leer data
excel_file = 'Datasets.xlsx'
sheet1,sheet2,sheet3 = 'AutoInsuranceSweden','WineQualityDataset','PimaIndiansDiabetesDataset'

data_1 = pd.read_excel(excel_file,sheet_name=sheet1)
#print(data)

data_2 = pd.read_excel(excel_file,sheet_name=sheet2)
#print(data_2)

data_3 = pd.read_excel(excel_file,sheet_name=sheet3)
#print(data)

#Dividir los datos en features y target
#Auto Insurance in Sweden ais
features_ais = data_1.drop('Y',axis=1)
target_ais = data_1['Y']
# print(features_ais)
# print(target_ais)

#Wine Quaality
features_wine = data_2.drop(columns='quality')
target_wine = data_2['quality']
# print(features_wine)
# print(target_wine)

#Pima Indians Diabetes Database
features_diabetes = data_3.drop(columns='Class variable (0 or 1)')
target_diabetes = data_3['Class variable (0 or 1)']
# print(features_wine)
# print(target_diabetes)

#Dividir los datos en training y testing
x_train, x_test, y_train, y_test = train_test_split(features_diabetes, target_diabetes, test_size=0.2, random_state=42)


#analizar datos con los métodos
#Regresión logística (Logistic Regression)
#Óptima para el dataset Pima Indians Diabetes Database dado que los datos de entrada son continuos y el de salida es binario
#Iniciar
log_regression = LogisticRegression(max_iter=200)

#Entrenar
log_regression.fit(features_diabetes,target_diabetes)

#Predecir
y_pred = log_regression.predict(x_test)
print(y_pred)
#K-Vecinos Cercanos (K-Nearest Neighbors)

#Maquinas Vector Soporte (Support Vector Machines)

#Naive Bayes
#Óptimo para el dataset Auto Insourance Sweden

#Iniciar
naive_bayes = GaussianNB()

#Entrenar
#naive_bayes.fit(x_train,y_train)

#Predecir
#y_pred = naive_bayes.predict(x_test)

#Red neuronal

#imprimir resultados
#accuracy = accuracy_score(y_test, y_pred)
#print("Accuracy:", accuracy)

# Mostrar el reporte de clasificación
#print(classification_report(y_test, y_pred))
