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

#######################################################################

def codificar(mensaje, cadena):
    mensaje_codificado = ""
    for letra in mensaje:
        if letra.isalpha():
            indice = ord(letra.lower()) - 97
            mensaje_codificado += cadena[indice]
        else:
            mensaje_codificado += letra
    return mensaje_codificado

def decodificar(mensaje_codificado, cadena):
    mensaje_decodificado = ""
    for letra in mensaje_codificado:
        if letra.isalpha():
            indice = cadena.index(letra.lower())
            mensaje_decodificado += chr(indice + 97)
        else:
            mensaje_decodificado += letra
    return mensaje_decodificado
##########################################################################
import random

def codificar(texto):
    caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=[]{}|;:,.<>/?'
    texto_codificado = ''
    for letra in texto:
        if letra.isalpha():
            if letra.isupper():
                texto_codificado += caracteres[(caracteres.index(letra) + 3) % len(caracteres)]
            else:
                texto_codificado += caracteres[(caracteres.index(letra) + 29) % len(caracteres)]
        elif letra.isdigit():
            texto_codificado += caracteres[(caracteres.index(letra) + 45) % len(caracteres)]
        else:
            texto_codificado += letra
    return texto_codificado

def decodificar(texto):
    caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=[]{}|;:,.<>/?'
    texto_decodificado = ''
    for letra in texto:
        if letra.isalpha():
            if letra.isupper():
                texto_decodificado += caracteres[(caracteres.index(letra) - 3) % len(caracteres)]
            else:
                texto_decodificado += caracteres[(caracteres.index(letra) - 29) % len(caracteres)]
        elif letra.isdigit():
            texto_decodificado += caracteres[(caracteres.index(letra) - 45) % len(caracteres)]
        else:
            texto_decodificado += letra
    return texto_decodificado
