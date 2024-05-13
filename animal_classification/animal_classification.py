import pandas as pd
import warnings

from sklearn.neighbors import KNeighborsClassifier, kneighbors_graph
from sklearn.linear_model import LogisticRegression 
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split 
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

class_name = pd.read_csv('class.csv')['Class_Type']

def get_features_target(dataset,lbl_target: str):
    features = dataset.drop(columns=lbl_target)
    target = dataset['class_type']
    return features,target

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
    print('\n')

def get_metrics(y_test,y_predict):
    metrics = []
    metrics.append("{:.2f}".format(accuracy_score(y_test, y_predict) * 100))
    metrics.append("{:.2f}".format(precision_score(y_test, y_predict, average='weighted', zero_division='warn') * 100))
    metrics.append("{:.2f}".format(recall_score(y_test, y_predict, average='weighted') * 100))
    metrics.append("{:.2f}".format(f1_score(y_test, y_predict, average='weighted') * 100))
    return metrics

def show_animal_class(animal_name, predictions):

    for (name,prediction) in zip(animal_name,predictions):
        print(name,': ',class_name[prediction-1])



warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=RuntimeWarning)

#leer data
excel_file = 'Datasets.xlsx'

#zoo.csv
zoo = pd.read_csv("zoo.csv")
zoo2 = pd.read_csv("zoo2.csv")
zoo3 = pd.read_csv("zoo3.csv")
zoo_full = pd.concat([zoo, zoo2, zoo3], ignore_index=True)

features, target = get_features_target(zoo_full,'class_type')
print('zoo.csv, zoo2.csv y zoo3.csv datasets combinados\n')
x_train, x_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
name_train,name_test = x_train['animal_name'],x_test['animal_name']
x_train, x_test = x_train.drop(columns='animal_name'),x_test.drop(columns='animal_name')

#Regresión logística
log_regression = LogisticRegression(max_iter=200)#Iniciar
log_regression.fit(x_train,y_train)#Entrenar
y_predict = log_regression.predict(x_test)#Predecir


#imprime los valores reales
print("Mostrar valores reales\n")
show_animal_class(name_test,y_test)
print('\n')
#imprime las predicciones
print("Mostrar predicciones. Logistic Regression\n")
show_animal_class(name_test,y_predict)

metrics = get_metrics(y_test,y_predict)
print_results('Regresión logística - métricas',metrics)

#K-Neighbors
k_neighbors = KNeighborsClassifier()#Iniciar
k_neighbors.fit(x_train,y_train)#Entrenar
y_predict = k_neighbors.predict(x_test)#Predecir

print("Mostrar predicciones. K-Vecinos Cercanos \n")
show_animal_class(name_test,y_predict)

metrics = get_metrics(y_test,y_predict)
print_results('K-Vecinos Cercanos - métricas',metrics)

#Maquinas Vector Soporte
svc = SVC()#Iniciar
svc.fit(x_train,y_train)#Entrenar
y_predict = svc.predict(x_test)#Predecir

print("Mostrar predicciones. Maquinas Vector Soporte \n")
show_animal_class(name_test,y_predict)

metrics = get_metrics(y_test,y_predict)
print_results('Maquinas Vector Soporte - métricas',metrics)

#Naive Bayes
naive_bayes = GaussianNB()#Iniciar
naive_bayes.fit(x_train,y_train)#Entrenar
y_predict = naive_bayes.predict(x_test)#Predecir

print("Mostrar predicciones. Naive Bayes\n")
show_animal_class(name_test,y_predict)

metrics = get_metrics(y_test,y_predict)
print_results('Naive Bayes - métricas',metrics)

#MLPClassifier
mlp_classifier = MLPClassifier()#Iniciar
mlp_classifier.fit(x_train,y_train)#Entrenar
y_predict = mlp_classifier.predict(x_test)#Predecir

print("Mostrar predicciones. MLPClassifier\n")
show_animal_class(name_test,y_predict)

metrics = get_metrics(y_test,y_predict)
print_results('MLPClassifier - métricas',metrics)