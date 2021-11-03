

def crearMatrisString(f,c):
    matrix=[]
    for i in range(f):
        MatrixAux=[""]*c
        matrix.append(MatrixAux)
    return matrix



mi_matrix=crearMatrisString(2,2)
mi_matrix[0][0]="alexander"
mi_matrix[0][1]="aviles"
print(mi_matrix)