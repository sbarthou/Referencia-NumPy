"""
en cada turno, tanto el profesor como cada alumno tiran el dado. El número obtenido por el profesor se compara con el de cada alumno y 
se hace lo siguiente: si el profesor saca un número mayor entonces le saca una ficha a los alumnos, si son iguales no pasa nada y si 
el alumno saca un número mayor entonces le saca una ficha al profesor. El juego continúa hasta que alguien, los alumnos o el profesor, 
queda con cero fichas. Si es el profesor entonces todos los alumnos ganan 5 décimas en el examen. De lo contrario pierden 1 décima.
Cree una función en Python llamada juego, que reciba como parámetros el número de alumnos y la cantidad de fichas, 
simule el tiro de los dados con números aleatorios entre 1 y 6 y guarde en una matriz cada una de las jugadas de los estudiantes asociando 
el número del estudiante con el resultado obtenido (Ganó, Perdió, Empate). Una vez terminado todo el proceso debe mostrarse la matriz con 
todas las jugadas y la función deberá retornar True si ganan los alumnos o False si pierden.
"""

import numpy as np
import random

def juego(alumnos, fichas):
    fAlumnos = fichas
    fProfesor = fichas
    while fAlumnos > 0 and fProfesor > 0:
        for i in range(alumnos):
            dAlumno = random.randrange(7)
            dProfesor = random.randrange(7)
            if dAlumno > dProfesor:
                fProfesor -= 1
                print(i+1, "Ganó")
            elif dAlumno < dProfesor:
                fAlumnos -= 1
                print(i+1, "Perdió")
            else:
                print(i+1, "Empate")
            if fAlumnos == 0 or fProfesor == 0:
                break
    if fProfesor == 0:
        return True
    elif fAlumnos == 0:
        return False
        
num_alumnos = int(input("Número de alumnos: "))
num_fichas = int(input("Número de fichas: "))

if juego(num_alumnos, num_fichas) is True:
    print("Los alumnos ganan 5 decimas!")
elif juego(num_alumnos, num_fichas) is False:
    print("Los alumnos pierden 1 decima")