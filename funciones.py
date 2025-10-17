"""
Asi se define una funcion
def nombre_de_funcion(parámetros):
    # código a ejecutar
    return resultado
"""

#definicion de funcion
def saludar():
    print("Hola, bienvenido a Python")

saludar()

#parametros y valores de retorno
def sumar(a, b):
    resultado = a + b
    return resultado

total = sumar(5, 3)
print("La suma es:", total)

#funciones con parametros por defecto
def saludar(nombre = "invitado"):
    print(f"Hola, {nombre}")

saludar("Alex")
saludar()

#funcion scope o alcance
#variable local
def mostrar_numero():
    x = 10 #variable local
    print("Dentro de la funcion:",  x)

mostrar_numero()
#print(x) #esta variable da error al imprimir porque esta en la funcion y no se la puede usar fuera de la funcion

#variable global
x = 100

def mostrar():
    print("Dentro de la funcion:", x)

mostrar()
print("Fuera de la funcion:", x)