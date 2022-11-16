"""
Un cuadrado mágico UAI es un cuadrado donde la suma de los elementos de la primera fila, de la primera columna y 
de la diagonal principal (la que va de izquierda a derecha) es la misma.
Escribe la función es_magico en Python que determine si un arreglo de nxn es un cuadrado mágico UAI.
"""

import numpy as np

def es_magico(a):
    if a.shape[0] == a.shape[1]:
        if sum(a[0]) == sum(np.diag(a)) == sum(a[:,0]):
            return True
        else:
            return False
    else:
        return False

# filas = int(input("Número de filas: "))
# columnas = int(input("Número de columnas: "))
# rango = int(input("Hasta que número será el rango de valores aleatorios: "))

# matriz = np.random.randint(0,rango,[filas,columnas])
# print(es_magico(matriz))