import os
os.system('cls')

mat1 = [
    [1, 0, 1],
    [0, 1, 2]
]
mat2 = [
    [3, 5],
    [-1, 0],
    [2, 1]
]

def multiplicarMat(matA = mat1, matB = mat2):
    if (len(matA[0]) == len(matB)):
        for index in range(0, len(matA)):
            for jindex in range(0, len(matA[index])):
                print(matA[index][jindex])

    return 'cosa'

print(multiplicarMat(mat1, mat2))

""" print(multiplicarMat(mat2, mat1)) """
