"""
Escribe un programa en Python que cree una matriz cuadrada de nxn (el valor de n es seleccionado por el usuario) 
con valores aleatorios en el rango [0,1] y que luego despliegue por pantalla:
- un arreglo 1D que contenga el promedio de las columnas de la matriz cuadrada.
- la matriz invertida.
- el resultado de la multiplicación de la matriz original consigo misma. La multiplicación de dos matrices.
cuadradas de tamaño n es otra matriz cuadrada de las mismas dimensiones:
donde C[i,j]=A[i,1]*B[1,j]+A[i,2]*B[2,j]+…+A[i,n]*B[n,j]

Para esto debes implementar y usar las siguientes funciones:
 
- promedio_columnas: que recibe como argumento de entrada la matriz de números y retorna 
un arreglo 1D donde cada casilla corresponde al promedio de una columna de la matriz.
- matriz_invertida: que recibe una matriz e imprime la matriz invertida.
- multiplica_matriz: que recibe como argumento de entrada la matriz de números y 
retorna la matriz con el resultado de la multiplicación de la matriz consigo misma.
"""

import numpy as np

def prom_columnas(a):
    b = []
    for i in range(a.shape[0]):
        b.append(np.mean(a[:,i]))
    b = np.array(b)
    return b.round(2)

def matriz_invertida(a):
    b = np.linalg.inv(a)
    return b.round(2)

def multiplica_matriz(a):
    b = a
    for i in range(a.shape[0]):
        for j in range(a.shape[0]):
            b[i,j] = a[i,j]*a[i,j]
            return b.round(2)

dim = int(input("Matriz cuadrada de dimension: "))
matriz = np.random.uniform(0,1,[dim,dim])

print(prom_columnas(matriz))
print(matriz_invertida(matriz))
print(multiplica_matriz(matriz))