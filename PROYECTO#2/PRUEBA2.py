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