def valInt (var, intervalo=None):

    if type(var)==int and intervalo==None:
        return True
    
    elif type(var)==int and type(intervalo)== tuple:
        if (var > intervalo[0] and var < intervalo[1]):
            return True
        else:
            return False
      
    elif type(var)==int and type(intervalo) == list and (var >= intervalo[0] and var <= intervalo[1]):
        if  (var >= intervalo[0] and var <= intervalo[1]):
            return True
        else:
            return False
      
    elif  type(var)==int and not (type(intervalo)==list or type(intervalo)==tuple):
        return TypeError
    
    elif type(var)==int and (intervalo[0]>=intervalo[1]):
        return ValueError

    else:
        return False
    

def valFloat (var, intervalo=None):

    if type(var)==float and intervalo==None:
        return True
    
    elif type(var)==float and type(intervalo)== tuple:
        if (var > intervalo[0] and var < intervalo[1]):
            return True
        else:
            return False
      
    elif type(var)==float and type(intervalo) == list and (var >= intervalo[0] and var <= intervalo[1]):
        if  (var >= intervalo[0] and var <= intervalo[1]):
            return True
        else:
            return False
      
    elif  type(var)==float and not (type(intervalo)==list or type(intervalo)==tuple):
        return TypeError
    
    elif type(var)==float and (intervalo[0]>=intervalo[1]):
        return ValueError

    else:
        return False
    
def multiplicar_matrices(matriz_1, matriz_2):
    resultado = []
    for i in range(len(matriz_1)):
        fila = []
        for j in range(len(matriz_2[0])):
            suma = 0
            for k in range(len(matriz_2)):
                suma += matriz_1[i][k] * matriz_2[k][j]
            fila.append(suma)
        resultado.append(fila)
    return resultado

matriz1 = [[1, 2, 3], [3, 4, 5], [3, 2, 5]]
matriz2 = [[5, 6, 7], [7, 8, 9], [7, 5, 9]]
print(multiplicar_matrices(matriz1, matriz2))