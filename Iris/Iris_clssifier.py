import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split as tts, LeaveOneOut, KFold,cross_val_score
from sklearn.neural_network import MLPClassifier as mlp
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import warnings

warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=RuntimeWarning)

dataset = pd.read_csv('irisbin.csv', header=None)
features = dataset.drop(axis=0,columns=[4,5,6])
target = dataset.iloc[:, 4:]
labels = ['setosa' if r[4] == -1 and r[5] == -1 and r[6] == 1
          else 'versicolor' if r[4] == -1 and r[5] == 1 and r[6] == -1
          else 'virginica'
          for _, r in target.iterrows()]

x_train, x_test, y_train, y_test = tts(features,labels, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(x_train)
X_test_scaled = scaler.transform(x_test)
# Define the number of hidden layers and neurons per layer
n_hidden_layers = 3 # Number of hidden layers
neurons_per_layer = 100  # Number of neurons per hidden layer

# Construct the tuple for hidden_layer_sizes parameter
hidden_layer_sizes = tuple([neurons_per_layer] * n_hidden_layers)
# model = mlp(hidden_layer_sizes=hidden_layer_sizes, activation='logistic', solver='adam', random_state=42, max_iter=1000)
model = mlp()
model.fit(X_train_scaled,y_train)
# model.fit(x_train,y_train)
y_predict = model.predict(X_test_scaled)
# y_predict = model.predict(x_test)

# Validación cruzada con LeaveOneOut
loo = LeaveOneOut()
scores_loo = cross_val_score(model, features, labels, cv=loo)
mean = scores_loo.mean()
std_dev = np.std(scores_loo)
expected_error = np.mean(np.abs(scores_loo-mean))
print("LeaveOneOut Proemedio:", mean)
print("LeaveOneOut Desviación estandar:", std_dev)
print("LeaveOneOut Error esperado:", expected_error)

# Validación cruzada con KFold
kf = KFold(n_splits=2)
scores_kf = cross_val_score(model, features, labels, cv=kf)
mean = scores_kf.mean()
std_dev = np.std(scores_kf)
expected_error = np.mean(np.abs(scores_kf-mean))
print("KFold CV  Proemedio:", mean)
print("KFold CV  Desviación estandar:", std_dev)
print("KFold CV  Error esperado:", expected_error)

print("Predicciones y Especies Reales:")
# x_test = x_test.iloc[:,:]
for i, (label, lbl_predict) in enumerate(zip(labels, y_predict)):
    print(f"A:{x_test.iloc[i][0]},B:{x_test.iloc[i][1]},C:{x_test.iloc[i][2]},D:{x_test.iloc[i][3]}: Predicción={lbl_predict}, Especie real={label}")

scaler = StandardScaler()
X_scaled = scaler.fit_transform(x_test)
# Aplicar PCA para reducir la dimensionalidad a 2 dimensiones
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
# Crear un DataFrame con las componentes principales
principal_components = pd.DataFrame(data=X_pca, columns=['PC1', 'PC2'])
principal_components['target'] = y_predict
markers = {'setosa': '1', 'versicolor': '+', 'virginica': 'x'}
# Visualizar los datos en un gráfico de dispersión
plt.figure(figsize=(8, 6))

for target_value in principal_components['target'].unique():
    subset = principal_components[principal_components['target'] == target_value]
    plt.scatter(subset['PC1'], subset['PC2'], marker=markers[target_value], label=target_value, alpha=0.5)

plt.title('irisbin.csv')
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')
plt.grid(True)
plt.show()