
def cargar_datos():
      cont=0
      n=0
      verda=True
      matrix=crearMatrisString(CantCuentas(),4)
      while(verda):
          try:
              aux=""
              aux+="cuentas\cuenta_"+str(cont)+".txt"
              miFile=open(aux,'r+')
              matrix[n][0] = miFile.readline()
              matrix[n][0 ]= matrix[n][0][0:len(matrix[n][0])-1]
              matrix[n][1] = miFile.readline()
              matrix[n][1] =matrix[n][1][0:len(matrix[n][1])-1]
              matrix[n][2] = miFile.readline()
              matrix[n][2] = matrix[n][2][0:len(matrix[n][2])-1]
              matrix[n][3] = miFile.readline()
              matrix[n][3] = matrix[n][3][0:len(matrix[n][3])-1]
          except FileNotFoundError:
            verda=False
          cont+=1
          n+=1
      return matrix

def CantCuentas():
    verda=True
    cont=0
    while(verda):
        try:
            aux = ""
            aux += "cuentas\cuenta_" + str(cont) + ".txt"
            cont += 1
            arcivo=open(aux,"r")
        except FileNotFoundError:
            verda=False
    return  cont-1

def crearMatrisString(f,c):
    matrix=[]
    for i in range(f):
        MatrixAux=[""]*c
        matrix.append(MatrixAux)
    return matrix

def verificarCuenta(numeroCuenta):
    global matrixCuentas
    global CantCuentasN
    for i in range(CantCuentasN):
        if numeroCuenta == matrixCuentas[i][1]:
            return True





#main paguina principal de variables globales etc
matrixCuentas=cargar_datos()
CantCuentasN=CantCuentas()
