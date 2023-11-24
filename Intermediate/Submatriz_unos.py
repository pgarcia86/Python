def submatriz_unos(matrix):
    #UNA SUBMATRIZ DE UNOS CUADRADA, ES CUADRADA SI LAS 3 POSICIONES QUE LO RODEAN SON UN 1
    matrix_aux = matrix

    '''
    len(matrix_aux) me devuelve la cantidad de filas
    len(matrix_aux[i]) me devuelve la cantidad de columnas
    '''

    for i in range(1, len(matrix_aux)):
        for j in range(1, len(matrix_aux[0])):
            if matrix_aux[i][j] == 1 and matrix_aux[i-1][j-1] != 0 and matrix_aux[i-1][j] != 0 and matrix_aux[i][j-1] != 0:
                matrix_aux[i][j] = min(matrix_aux[i-1][j-1], matrix_aux[i-1][j], matrix_aux[i][j-1]) + 1
    print(max(max(matrix_aux)))

matriz_ejemplo = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1], 
    [1, 1, 0, 0, 0, 0, 0]
]

submatriz_unos(matriz_ejemplo)