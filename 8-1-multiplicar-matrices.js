const mat1 = [
    [1, 0, 1],
    [0, 1, 2]
]
const mat2 = [
    [3, 5],
    [-1, 0],
    [2, 1]
]

const traspasarMat = (matriz) => {
    const res = [];
    for(let fila = 0; fila < matriz[0].length; fila++) {
        res[fila] = []
        for(let columna = 0; columna < matriz.length; columna++) {
            res[fila][columna] = matriz[columna][fila]
        }
    }
    return res;
}
console.log(traspasarMat(mat2));

const multiplciarMat = (matrizA = mat1, matrizB=mat2) => {
    const longitud = matrizA[0].length
    const tras = traspasarMat(mat2);
    const res = []

    for(let index = 0; index < matrizA.length; index++) {
        for(let jindex = 0; jindex < matrizA[index].length; jindex++) {
            const item = matrizA[index][jindex] * tras[index][jindex]
            
        }
    }

    return res
}

console.log(multiplciarMat(mat1, mat2))

