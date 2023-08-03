def valList (var, lista=None, letra=None):

    if type(letra) != str:
        if type(lista)!=int and type(letra)!=str:
            return TypeError
        elif type(lista)!=list and type(letra)!=str:
            return TypeError

    elif type(letra)!= 'list' or type(letra)!= 'value':
        return ValueError

    else:
        return False

print("**", valList(5,[1,2],9)) #typeerror
print(valList(5,4,'hola')) #valueerror