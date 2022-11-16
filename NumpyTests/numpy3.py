# Escribe un programa en Python que cree una lista de números aleatorios enteros entre 0 y 1000 (que llamaremos lista original) 
# y una variable (k) entera aleatoria entre 0 y 1000. El tamaño de la lista original se le debe solicitar al usuario.  
# Posteriormente, el programa debe imprimir por pantalla:
# - el contenido de la lista original
# - el valor de k
# - el contenido de una lista que almacena todos los valores de la lista original que son mayores a k
# - el número de valores de la lista original que son iguales a k
# - el contenido de una lista que almacena todos los valores de la lista original que son menores a k
#
# En tu programa debes implementar y usar las siguientes funciones:
#
# - lista_aleatorios: que recibe como argumento de entrada el tamaño de la lista original y retorna esta lista
# - operadores: que recibe como argumento de entrada la lista original y el número aleatorio k y retorna la lista 
#   con los números mayores a k, la lista con los números menores a k y el número de elementos de la lista original iguales a k.

import numpy as np
import random

def lista_aleatorios(dim):
    listaOriginal = np.random.randint(0, 1001, [dim])
    return listaOriginal

def operadores(listaOriginal, k):
    mayores = []
    menores = []
    iguales = []
    for i in range(len(listaOriginal)):
        if listaOriginal[i] > k:
            return mayores.append(listaOriginal[i])
        if listaOriginal[i] < k:
            return menores.append(listaOriginal[i])
        if listaOriginal[i] == k:
            return iguales.append(listaOriginal[i])

tamaño = int(input("Tamaño de la lista: "))
num_k = random.randrange(1001)
lista = lista_aleatorios(tamaño)

print(lista_aleatorios(tamaño))
print(operadores(lista, num_k))