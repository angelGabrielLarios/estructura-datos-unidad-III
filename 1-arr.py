def recorrerLista():
    miArr = [1, 2, 'angel', 'gabriel', 10, 2]
    for item in miArr:
        print(item)
""" recorrerLista() """

def imprimirItem():
    miArr = [1, 2, 'angel', 'gabriel', 10, 2]
    numeroElem = len(miArr)
    for index in range(0, numeroElem):
        item = miArr[index]
        print(item)

imprimirItem()
