'''
NumPy es una biblioteca ampliamente utilizada en Python para el
cálculo numérico y la manipulación de matrices y arreglos
multidimensionales. Proporciona una interfaz fácil de usar para realizar
operaciones matemáticas eficientes en datos numéricos.'''

import numpy as np
# Crear un arreglo de números
numeros = np.array([1, 2, 3, 4, 5])
# Calcular la suma de los elementos
suma = np.sum(numeros)
# Calcular el promedio de los elementos
promedio = np.mean(numeros)


'''
Pandas es una biblioteca popular utilizada para el análisis y
manipulación de datos tabulares en Python. Proporciona estructuras de
datos flexibles y eficientes, como el DataFrame, que permite realizar
operaciones complejas en conjuntos de datos.'''

import pandas as pd
# Crear un DataFrame
data = {
    'Nombre': ['Juan', 'María', 'Carlos'],
    'Edad': [25, 30, 35],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia']
}
df = pd.DataFrame(data)
# Mostrar los primeros registros del DataFrame
primeros_registros = df.head()
# Filtrar el DataFrame por una condición
filtro = df[df['Edad'] > 28]


'''
Matplotlib es una biblioteca de trazado en 2D ampliamente utilizada en
Python. Permite crear visualizaciones y gráficos de alta calidad para
explorar y comunicar datos de manera efectiva.'''

import matplotlib.pyplot as plt
# Datos de ejemplo
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
# Crear un gráfico de línea
plt.plot(x, y)
# Mostrar el gráfico
plt.show()


'''
Requests es una biblioteca popular en Python utilizada para realizar
solicitudes HTTP y trabajar con APIs web. Permite enviar y recibir datos
a través de Internet de manera sencilla y eficiente.'''

import requests
# Realizar una solicitud GET a una API
response=requests.get('https://api.example.com/data')
# Obtener los datos de la respuesta
data = response.json()
# Mostrar los datos
print(data)


