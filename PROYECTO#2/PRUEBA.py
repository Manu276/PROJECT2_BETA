#COMPLEX
def valComplex(var, intervalo = None):
    global mod_var
    mod_var = (var.real**2 + var.imag**2)**0.5
    print(mod_var)


    if type(var)==complex and intervalo==None:
        return True

    elif  type(var)==complex and intervalo==tuple:
        if (mod_var > intervalo[0] and mod_var < intervalo[1]):
            return True
        else:
            return False

    elif type(var)==complex and intervalo==list:
        if (mod_var >= intervalo[0] and mod_var <= intervalo[1]):
            return True
        else:
            return False
    
    elif type(var)==complex and not (type(intervalo)==tuple or type(intervalo)==list):
        return TypeError

    elif type(var)==complex and (intervalo[0]>=intervalo[1]):
        return ValueError

    else:
        return False

#print(valComplex(3+4j))
#print(valComplex(4.0))
#print(valComplex(3+4j,(5,10)))
print(valComplex(3+4j,[5, 10]))
print(valComplex(3+4j,[4, 10]))
#print(valComplex(3+4j,[10,4]))
#print(valComplex(3+4j,5))
