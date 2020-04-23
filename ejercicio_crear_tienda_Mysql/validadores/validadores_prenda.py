import re
expresion_talla = "^[0-9]{1,3}$"
expresion_color = "^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]{2,20}$"
expresion_marca = "^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]{2,20}$"
expresion_tipo = "^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]{2,20}$"


def validar_talla(talla):
    validador = re.compile(expresion_talla)
    return validador.match(talla)

def validar_color(color):
    validador = re.compile(expresion_color)
    return validador.match(color)

def validar_marca(marca):
    validador = re.compile(expresion_marca)
    return validador.match(marca)

def validar_tipo(tipo):
    validador = re.compile(expresion_tipo)
    return validador.match(tipo)



