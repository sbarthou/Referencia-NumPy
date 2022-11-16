"""
La UAI organizó un campeonato de básquetbol y desea conocer el rendimiento que obtuvo cada equipo. Para ello ha creado una matriz 
donde cada fila corresponde a un equipo. Cada fila (equipo) tiene 3 columnas: la columna 0 almacena el número de partidos ganados, 
la columna 1 el número de partidos empatados y la columna 2 el número de partidos perdidos.
Escribe una función llamada rendimiento que recibe como parámetro esta matriz y retorna un arreglo 1D con el rendimiento de cada equipo. 
El rendimiento de un equipo se calcula como:
Rendimiento = (3*Partidos Ganados + Partidos Empatados ) / (3*Total de Partidos Jugados )
"""

import numpy as np

def rendimiento(matriz):
    lista = []
    for i in range(matriz.shape[0]):
        formula = 3*(matriz[i,0] + matriz[i,1])/(3*(matriz[i,2]))
        lista.append(formula)
    return lista

fila = int(input("Número de equipos: "))
datos = np.random.randint(1, 6, [fila, 3])
print(rendimiento(datos))