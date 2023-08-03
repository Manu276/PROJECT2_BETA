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

print(valInt(4)) #True
print(valInt(4.0)) #False
print(valInt(4,(4,10))) #False
print(valInt(4,[3,9])) #True
print(valInt(4,[4,10])) #True
print(valInt(4,[10,4])) #ValueError
print(valInt(4,5)) #TypeError
    

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
    


print(valFloat(4.0)) #True
print(valFloat(4)) #False
print(valFloat(4.4,(4.4,10))) #False
print(valFloat(4.4,(4,10))) #True
print(valFloat(4.1,[4.1,9.05])) #True
print(valFloat(4.2,[4,10])) #True
print(valFloat(4.4,[10,4])) #ValueError 
print(valFloat(4.0,5)) #TypeError
    
#COMPLEX
def valComplex(var, intervalo = None):
  
    mod_var = ((var.real)**2 + (var.imag**2))**0.5

    mod_var=int(mod_var)

    if type(var)==complex and intervalo==None:
        return True

    elif  type(var)==complex and intervalo==tuple:
        if (mod_var > intervalo[0] and mod_var < intervalo[1]):
            return True


    elif type(var)==complex and type(intervalo)==list:
        if (mod_var >= intervalo[0] and mod_var <= intervalo[1]):
            return True

    
    elif type(var)==complex and not (type(intervalo)==tuple or type(intervalo)==list):
        return TypeError

    elif type(var)==complex and (intervalo[0]>=intervalo[1]):
        return ValueError

    else:
        return False

print(valComplex(3+4j)) #True
print(valComplex(4.0)) #False
print(valComplex(3+4j,(5,10)))#False
print(valComplex(3+4j,[5,10]))#True
print(valComplex(3+4j,[4,10]))#True
print(valComplex(3+4j,[10,4])) #ValueError
print(valComplex(3+4j,5)) #TypeError




##LIST

def valList (var, lista=None, letra=None):

    if type(var)==list and lista==None and letra==None:
        return True

    elif letra=='value' and type(var)==list and type(lista)==list and set(var)==set(lista):

            return True

    
    elif letra=='len' and type(var)==list and type(lista)==int and len(var)==lista:
        return True

    elif type(var)!=list:
        return False
    
    if type(letra) != str:
        if type(lista)!=int and type(letra)!=str:
            return TypeError
        elif type(lista)!=list and type(letra)!=str:
            return TypeError

    elif type(letra)!= 'list' or type(letra)!= 'value':
        return ValueError


    else:
        return False



print(valList([1,2,3])) #true
print(valList([1,2,3,4],[1,3,2,4],'value')) #true
print(valList([1,2,3],3,'len')) #true
print("*", valList(5)) #false
print(valList(5,2,'value')) #false
print(valList(5,7,'len')) #false
print("**", valList(5,[1,2],9)) #typeerror
print(valList(5,4,'hola')) #valueerror
