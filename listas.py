numeros = [1, 2, 3, 4, 5]
print("Tercer elemento:", numeros[2])

numeros.append(6)
print("Despues de append:", numeros)

numeros.remove(3)
print("Despues de remove(3):", numeros)

numeros.sort()
print("Ordenados ascendente:", numeros)

numeros.sort(reverse=True)
print("Ordenados descendente:", numeros)

print("Dos primeros elementos:", numeros[:2])

print("Dimension lista:", len(numeros))