import pandas as pd
import warnings

from sklearn.neighbors import KNeighborsClassifier, kneighbors_graph
from sklearn.linear_model import LogisticRegression 
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split 
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def categorizar_y(y):
    if y <= quartiles.iloc[0]:
        return 'c'
    elif y > quartiles.iloc[0] and y <= quartiles.iloc[1]:
        return 'b'
    else:
        return 'a'

def print_results(clasificador,metrics):
    print("\nClasificador: ",clasificador)
    print("Accuracy: ", metrics[0],"%")
    print("Precision:", metrics[1],"%")
    print("Recall:", metrics[2],"%")
    print("F1 Score:", metrics[3],"%")

def get_metrics(y_test,y_predict):
    metrics = []
    metrics.append("{:.2f}".format(accuracy_score(y_test, y_predict) * 100))
    metrics.append("{:.2f}".format(precision_score(y_test, y_predict, average='weighted', zero_division='warn') * 100))
    metrics.append("{:.2f}".format(recall_score(y_test, y_predict, average='weighted') * 100))
    metrics.append("{:.2f}".format(f1_score(y_test, y_predict, average='weighted') * 100))
    return metrics

warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=RuntimeWarning)

#leer data
excel_file = 'Datasets.xlsx'
sheet1,sheet2,sheet3 = 'AutoInsuranceSweden','WineQualityDataset','PimaIndiansDiabetesDataset'

data_1 = pd.read_excel(excel_file,sheet_name=sheet1)
quartiles = data_1['Y'].quantile([0.25,0.5,0.75])

data_1['categoria_y'] = data_1['Y'].apply(categorizar_y)

data_2 = pd.read_excel(excel_file,sheet_name=sheet2)

data_3 = pd.read_excel(excel_file,sheet_name=sheet3)

#Auto Insurance in Sweden
print('Auto Insurance in Sweden')
features_ais = data_1[['X']]
target_ais = data_1['categoria_y']
x_train, x_test, y_train, y_test = train_test_split(features_ais, target_ais, test_size=0.2, random_state=42)

#Regresión logística
log_regression = LogisticRegression(max_iter=500)#Iniciar
log_regression.fit(x_train,y_train)#Entrenar
y_predict = log_regression.predict(x_test)#Predecir

metrics = get_metrics(y_test,y_predict)
print_results('Regresión logística',metrics)

#K-Neighbors
k_neighbors = KNeighborsClassifier()#Iniciar
k_neighbors.fit(x_train,y_train)#Entrenar
y_predict = k_neighbors.predict(x_test)#Predecir

metrics = get_metrics(y_test,y_predict)
print_results('K-Vecinos Cercanos',metrics)

#Maquinas Vector Soporte
svc = SVC()#Iniciar
svc.fit(x_train,y_train)#Entrenar
y_predict = svc.predict(x_test)#Predecir

metrics = get_metrics(y_test,y_predict)
print_results('Maquinas Vector Soporte',metrics)

#Naive Bayes
naive_bayes = GaussianNB()#Iniciar
naive_bayes.fit(x_train,y_train)#Entrenar
y_predict = naive_bayes.predict(x_test)#Predecir

metrics = get_metrics(y_test,y_predict)
print_results('Naive Bayes',metrics)

#MLPClassifier
mlp_classifier = MLPClassifier()#Iniciar
mlp_classifier.fit(x_train,y_train)#Entrenar
y_predict = mlp_classifier.predict(x_test)#Predecir

metrics = get_metrics(y_test,y_predict)
print_results('MLPClassifier',metrics)

#Wine Quality
print('\nWine Quality')
features_wine = data_2.drop(columns='quality')
target_wine = data_2['quality']
x_train, x_test, y_train, y_test = train_test_split(features_wine, target_wine, test_size=0.2, random_state=42)

#Regresión logística
log_regression = LogisticRegression(max_iter=200)#Iniciar
log_regression.fit(x_train,y_train)#Entrenar
y_predict = log_regression.predict(x_test)#Predecir

metrics = get_metrics(y_test,y_predict)
print_results('Regresión logística',metrics)

#K-Neighbors
k_neighbors = KNeighborsClassifier()#Iniciar
k_neighbors.fit(x_train,y_train)#Entrenar
y_predict = k_neighbors.predict(x_test)#Predecir

metrics = get_metrics(y_test,y_predict)
print_results('K-Vecinos Cercanos',metrics)

#Maquinas Vector Soporte
svc = SVC()#Iniciar
svc.fit(x_train,y_train)#Entrenar
y_predict = svc.predict(x_test)#Predecir

metrics = get_metrics(y_test,y_predict)
print_results('Maquinas Vector Soporte',metrics)

#Naive Bayes
naive_bayes = GaussianNB()#Iniciar
naive_bayes.fit(x_train,y_train)#Entrenar
y_predict = naive_bayes.predict(x_test)#Predecir

metrics = get_metrics(y_test,y_predict)
print_results('Naive Bayes',metrics)

#MLPClassifier
mlp_classifier = MLPClassifier()#Iniciar
mlp_classifier.fit(x_train,y_train)#Entrenar
y_predict = mlp_classifier.predict(x_test)#Predecir

metrics = get_metrics(y_test,y_predict)
print_results('MLPClassifier',metrics)

#Pima Indians Diabetes Database
print('\nPima Indians Diabetes Database')
features_db = data_3.drop(columns='Class variable (0 or 1)')
target_db = data_3['Class variable (0 or 1)']
x_train, x_test, y_train, y_test = train_test_split(features_db, target_db, test_size=0.2, random_state=42)

#Regresión logística
log_regression = LogisticRegression(max_iter=200)#Iniciar
log_regression.fit(x_train,y_train)#Entrenar
y_predict = log_regression.predict(x_test)#Predecir

metrics = get_metrics(y_test,y_predict)
print_results('Regresión logística',metrics)

#K-Neighbors
k_neighbors = KNeighborsClassifier()#Iniciar
k_neighbors.fit(x_train,y_train)#Entrenar
y_predict = k_neighbors.predict(x_test)#Predecir

metrics = get_metrics(y_test,y_predict)
print_results('K-Vecinos Cercanos',metrics)

#Maquinas Vector Soporte
svc = SVC()#Iniciar
svc.fit(x_train,y_train)#Entrenar
y_predict = svc.predict(x_test)#Predecir

metrics = get_metrics(y_test,y_predict)
print_results('Maquinas Vector Soporte',metrics)

#Naive Bayes
naive_bayes = GaussianNB()#Iniciar
naive_bayes.fit(x_train,y_train)#Entrenar
y_predict = naive_bayes.predict(x_test)#Predecir

metrics = get_metrics(y_test,y_predict)
print_results('Naive Bayes',metrics)

#MLPClassifier
mlp_classifier = MLPClassifier()#Iniciar
mlp_classifier.fit(x_train,y_train)#Entrenar
y_predict = mlp_classifier.predict(x_test)#Predecir

metrics = get_metrics(y_test,y_predict)
print_results('MLPClassifier',metrics)
