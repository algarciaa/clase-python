ciudades = ("Quito", "Guayaquil", "Cuenca")

print("Segunda Ciudad:", ciudades[1])

try:
    ciudades[0] = "Ambato"
except TypeError as e:
    print("Error:", e)

ciudades_lista = list(ciudades)
ciudades_lista.append("Ambato")
ciudades = tuple(ciudades_lista)
print("Nueva tupla:", ciudades)