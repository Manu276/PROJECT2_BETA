import random

def generar_clave(): #se empieza a generar la clave aleatoria
    global letras #como se usa esta variable en las demas funciones se coloca global
    letras = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890 °~!¡@#$%^&*()_+-=[]{}|;':\",./<>¿?ƒö∞↓Äƒ"
    #se crea una base para crear la clave 
    clave = ''.join(random.sample(letras, len(letras))) #empezando con un str vacio se usa el join para poder unir las letras que va agarrando random con un sample que agarre la longitud de letras para colocar esa cantidad de terminos en la clave
    return clave

def codificar(mensaje, clave):
    mensaje_codificado = '' #se crea un str vacio 
    for letra in mensaje: #aqui va a recorrer el mensaje letra por letra 
        if letra in clave: #si la letra en el recorrido se encuentra 
            mensaje_codificado += clave[letras.index(letra)]# va concadenando las letras de la clave va a tomar la posicion de la letra dentro del string
        else:
            mensaje_codificado += letra #sino esta, simplemente la concadena
    return mensaje_codificado

def decodificar(mensaje_codificado, clave):
    mensaje_decodificado = ''
    for letra in mensaje_codificado: #Hace lo mismo pero a la inversa recorriendo el mensaje codificadoo
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

