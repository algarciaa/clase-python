numeros = (5, 8, 12, 3, 9, 5, 2)

#mostrar el valor maximo y minimo
maximo = max(numeros)
minimo = min(numeros)
print("Maximo", maximo)
print("Minimo", minimo)

#calcular el promedio
promedio = sum(numeros) / len(numeros)
print("Promedio:", round(promedio, 2))

#Verificar si mi numero esta dentro de la tupla
num_usuario = int(input("Ingrese un numero "))

if num_usuario in numeros:
    print("El numero esta dentro de la tupla")
else:
    print("El numero no esta dentro de la tupla")