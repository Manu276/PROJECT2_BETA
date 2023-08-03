#MODULO DE UN NUMERO COMPLEJO

#METODO 1
#{
var = complex(4+6j)

mod_var = abs(var)

print(mod_var)
#}

#METODO 2
#{
var="4-6j"
if "+" in var:
    a=float(var.split("+")[0])
    b=float(var.split("+")[1].replace("j", ""))
else:
    a=float(var.split("-")[0])
    b=float(var.split("-")[1].replace("j", ""))

mod_var=(a**2 + b**2)**0.5

print(mod_var)
#}

#METODO 3
#{
var = 3-4j
mod_var = (var.real**2 + var.imag**2)**0.5

print(mod_var)
#}

#METODO 4
#{
var = "4+6j"
var = complex(var)
mod_var = (var.real**2 + var.imag**2)**0.5

print(mod_var)

#}