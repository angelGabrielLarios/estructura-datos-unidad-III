""" 
Las lista en Python son un tipo de dato que permite almacenar datos de cualquier tipo
Son mutables y dinamicas, lo cual es la principal diferencia con los set y las tuplas
"""
""" import os
os.system('cls') """

lista = [1, 2, 3, 4]
""" lista de un mismo dato """
print('')
print(lista)
print('')

listaO = [3, 'Hola', True, 7.8]
""" lista de diferente tipos de dato """
print(listaO)


""" 
Acceder a las listas

Si tenemos una lista determinada con n elementos almacenados en ella, podemos acceder a los mismos
usando corchetes y un indice, que va desde 0 a n-1 siendo el tamaño de la lista
"""

print('')
colores = [
    "rojo",
    "azul",
    "morado",
    "verde"
]
print(colores)
print(colores[0])
print(colores[2])
""" 
Tambien puedes acceder con indices negativos
"""
print('')
print(colores[-1])
print(colores[-2])