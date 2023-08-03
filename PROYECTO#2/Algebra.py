def multiplicacion_matrices(matriz1, matriz2):
    filas_matriz1 = len(matriz1)
    columnas_matriz1 = len(matriz1[0])
    filas_matriz2 = len(matriz2)
    columnas_matriz2 = len(matriz2[0])

    if columnas_matriz1 != filas_matriz2:
        return "No es posible multiplicar las matrices. La cantidad de columnas de la Matriz 1 debe ser igual a la cantidad de filas de la matriz 2"    
    
    matriz_resultado = []

    for i in range(filas_matriz1):
        fila_resultado = []
        for j in range(columnas_matriz2):
            suma = 0
            for k in range(filas_matriz2):
                suma += matriz1[i][k] * matriz2[k][j]
            fila_resultado.append(suma)
        matriz_resultado.append(fila_resultado)

    return matriz_resultado


def producto_vectorial(vect_1, vect_2):
    x = vect_1[1] * vect_2[2] - vect_1[2] * vect_2[1]
    y = vect_1[2] * vect_2[0] - vect_1[0] * vect_2[2]
    z = vect_1[0] * vect_2[1] - vect_1[1] * vect_2[0]
    return [x, y, z]


def transpuesta(matriz):
    resultado = []

    for i in range(len(matriz[0])):
        fila = []

        for j in range(len(matriz)):
            fila.append(matriz[j][i])

        resultado.append(fila)
    return resultado


def determinante(matriz):
    if len(matriz)==2:
        resultado=matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    elif len(matriz)==3:
        a = matriz[0][0]
        b = matriz[0][1]
        c = matriz[0][2]
        d = matriz[1][0]
        e = matriz[1][1]
        f = matriz[1][2]
        g = matriz[2][0]
        h = matriz[2][1]
        i = matriz[2][2]
        resultado=a*e*i + b*f*g + c*d*h - c*e*g - b*d*i - a*f*h
    elif len(matriz)==4:
        a = matriz[0][0]
        b = matriz[0][1]
        c = matriz[0][2]
        d = matriz[0][3]
        e = matriz[1][0]
        f = matriz[1][1]
        g = matriz[1][2]
        h = matriz[1][3]
        i = matriz[2][0]
        j = matriz[2][1]
        k = matriz[2][2]
        l = matriz[2][3]
        m = matriz[3][0]
        n = matriz[3][1]
        o = matriz[3][2]
        p = matriz[3][3]
        resultado=a*f*k*p + a*g*l*n + a*h*j*o + b*e*l*p + b*g*i*o + b*h*k*n + c*e*j*p + c*f*i*o + c*h*g*m + d*e*k*n + d*f*j*m + d*g*i*l - d*e*l*o - d*f*k*n - d*g*j*p
    return resultado
