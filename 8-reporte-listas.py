
from operator import le
import os

os.system('cls')

Yo = 'angel gabriel'
AbuelosP = ['felipe', 'gabina']
AbuelosM = ['angel', 'cecilia']
Padres = ['regulo', 'sonia']
Hermanas = ['marisol']
Hermanos = None


familia = [Yo,AbuelosP,AbuelosM,Padres,Hermanas,Hermanos]
print(familia)

""" acceder a las siguiente posiciones de la lista familia """


print()
print(familia[0])

print()
print(familia[1][1])

print()
print(familia[3])

print()
print(familia[2][0])


""" 
Parte II
1. Escribir un programa que permita multiplicar una matriz de 2 * 2, recuerda
los pasos a seguir para una multiplicación de matrices. Recuerda guardar tu
archivo .py y tus capturas correspondientes.
"""


def multiplicarMatriz():
    A = [
        [6, 4],
        [8, 9]
    ]
    B = [
        [3, 2],
        [1, 7]
    ]
    res = [
        [
            (A[0][0] * B[0][0]) + (A[0][1] * B[1][0]),
            (A[0][0] * B[0][1]) + (A[0][1] * B[1][1])
        ],
        [
            (A[1][0] * B[0][0]) + (A[1][1] * B[1][0]),
            (A[1][0] * B[0][1]) + (A[1][1]* B[1][1])
        ]
    ]
    return res

print(multiplicarMatriz())

print()

""" 
Escribir un programa que te permita realizar la suma de dos matrices
cuadradas de 3 * 3. Recuerda guardar tu archivo .py y tus capturas
correspondientes. 
"""



matrizUno = [
    [2, 0, 1],
    [3, 0, 0],
    [5, 1, 1]
]

matrizDos = [
    [1, 0, 1],
    [1, 2, 1],
    [1, 1, 0]
]

def sumarMatrices(matrizA, matrizB):
    filaLongitud = len(matrizA)
    columnaLongitud = len(matrizA[0])
    res = []
    for fila in range(0, filaLongitud):
        nuevaFila = []
        for columna in range(0, columnaLongitud):
            item = matrizA[fila][columna] + matrizB[fila][columna] 
            nuevaFila.append(item)
        res.append(nuevaFila)
    return res

print(sumarMatrices(matrizUno, matrizDos))


arr1 = [
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3]
]

arr2 = [
    [3, 2, 1],
    [3, 0, 1],
    [3, 2, 1]
]


print()
print(sumarMatrices(arr1, arr2))







