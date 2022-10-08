

a_tuple = ('value1', 'value2', 'value3')

var1, var2, var3 = a_tuple

print(var1)
print(var2)
print(var3)

print()

autores = ('Verne', 'Murakami', 'Rowling')

autor1, autor2, autor3 = autores

print(autor1)
print(autor2)
print(autor3)

""" inter cambio de valores """

valor1 = 45
valor2 = 29

print()
print(f'valor 1 es  {valor1}')
print(f'valor 2 es  {valor2}')


valor1, valor2 = valor2, valor1
print()
print(f'valor 1 es  {valor1}')
print(f'valor 2 es  {valor2}')

nombre = (
    'M', 'A', 'C', 'U', 'I', 'L', 'X', 'O', 'C', 'H'
)

print()
print(nombre)

head, *body, tail = nombre

print(head)
print(body)
print(tail)


""" es extensible a cialqioer tipo de datos que sea iterable """

letrero = '¡Hola mundo!'

head, *body, tail = letrero
print()
print(head)
print(body)
print(tail)

""" los extensible tambien son aplicados para la listas"""


escritor1, escritor2, escritor3 = [
    'Jane Austen', 'J.K Rowing', 'Haruki Murakami'
]

print()
print(escritor1)
print(escritor2)
print(escritor3)


