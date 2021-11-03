#se cargar las cuentas de los archivos locales
def cargar_datos():
      cont=0
      n=0
      verda=True
      matrix=crearMatrisString(CantCuentas(),4)
      while(verda):
          try:
              File=""
              File+="cuentas\cuenta_"+str(cont)+".txt"
              miFile=open(File,'r+')
              matrix[n][0] = miFile.readline()
              matrix[n][0] = matrix[n][0][0:len(matrix[n][0])-1]
              matrix[n][1] = miFile.readline()
              matrix[n][1] = matrix[n][1][0:len(matrix[n][1])-1]
              matrix[n][2] = miFile.readline()
              matrix[n][2] = matrix[n][2][0:len(matrix[n][2])-1]
              matrix[n][3] = miFile.readline()
          except FileNotFoundError:
            verda=False
          cont+=1
          n+=1
      return matrix

def GuardarDatos():
    global numeroDeCuenta
    global matrixCuentas
    pos=buscarPoscuenta(numeroDeCuenta)
    File = ""
    File += "cuentas\cuenta_"+str(pos)+".txt"
    try:
        GuardarDatosFile=open(File , "w")
        auxDatosCuenta = matrixCuentas[pos][0] + "\n"
        auxDatosCuenta += matrixCuentas[pos][1] + "\n"
        auxDatosCuenta += matrixCuentas[pos][2] + "\n"
        auxDatosCuenta += matrixCuentas[pos][3]
        GuardarDatosFile.write(auxDatosCuenta)
        GuardarDatosFile.close()
    except FileNotFoundError:
        return False

#devuelve la cantidad de cuentas
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

#true si existe y false si no
def verificarCuenta(numeroCuenta):
    global matrixCuentas
    CantCuentasN=CantCuentas()
    for i in range(CantCuentasN):
        if numeroCuenta == matrixCuentas[i][1]:
            return True
    return False

#busca la posicion de la cuenta i retorna la pos y si no existe retorna -1
def buscarPoscuenta(numeroCuenta):
    global matrixCuentas
    numeroCuentafinal=0
    for i in range(CantCuentas()):
        if numeroCuenta == matrixCuentas[i][1]:
            return i
    return -1

#si es correcta de devuelve un true si no un false
def verificarPassword(contra):
    global numeroDeCuenta
    global matrixCuentas
    pos=buscarPoscuenta(numeroDeCuenta)
    if pos!=-1:
        print(matrixCuentas[pos][3])
        if matrixCuentas[pos][3] == contra:
            return True
    return False

#devuelve un True si esta correcto y un False si no hay fondos o esta mal el pass o la cuenta
def retirarDinero(cantDinero):
    global numeroDeCuenta
    global passDeCuenta
    global matrixCuentas
    dineroFloat=0
    if verificarCuenta(numeroDeCuenta):
        if verificarPassword(passDeCuenta):
            dineroFloat=float(matrixCuentas[buscarPoscuenta(numeroDeCuenta)][2])
            if dineroFloat>cantDinero:
                dineroFloat=dineroFloat-cantDinero
                matrixCuentas[buscarPoscuenta(numeroDeCuenta)][2]=str(dineroFloat)
                return True
            else:
                print("no hay suficientes fondos")
                return False
    return False


#variables globales y temporales etc
matrixCuentas=cargar_datos()
#flotantes
numeroDeCuenta="12345"
passDeCuenta="1234"


