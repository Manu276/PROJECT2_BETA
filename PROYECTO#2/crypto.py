import random

def generar_clave():
    global letras
    letras = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890 °~!¡@#$%^&*()_+-=[]{}|;':\",./<>¿?ƒö∞↓Äƒ"
    clave = ''.join(random.sample(letras, len(letras)))
    return clave

def codificar(mensaje, clave):
    mensaje_codificado = ''
    for letra in mensaje:
        if letra in clave:
            mensaje_codificado += clave[letras.index(letra)]
        else:
            mensaje_codificado += letra
    return mensaje_codificado

def decodificar(mensaje_codificado, clave):
    mensaje_decodificado = ''
    for letra in mensaje_codificado:
        if letra in clave:
            mensaje_decodificado += letras[clave.index(letra)]
        else:
            mensaje_decodificado += letra
    return mensaje_decodificado
clave = generar_clave()
mensaje = "Hola Mundo"
mensaje_codificado = codificar(mensaje, clave)
mensaje_decodificado = decodificar(mensaje_codificado, clave)

print("Clave: " , clave)
print("Mensaje original: " , mensaje)
print("Mensaje codificado: " , mensaje_codificado)
print("Mensaje decodificado: " , mensaje_decodificado)

