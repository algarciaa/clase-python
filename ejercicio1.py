numeros = [4, 7, 2, 4, 9, 2, 8, 6, 7]

#eliminar duplicados
sin_duplicados = list(set(numeros))
print("Lista sin duplicados:", sin_duplicados)

#ordenar de menor a mayor
ordenada = sorted(sin_duplicados)
print("Lista ordenada:", ordenada)

#mostrar solo los numeros pares
pares = [num for num in ordenada if num % 2 == 0]
print("Numeros pares:", pares)