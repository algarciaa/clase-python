persona = {"nombre": "Alex", "edad": 25, "ciudad": "Guayaquil"}
print("Diccionario inicial:", persona)

print("Edad:", persona.get("edad"))

persona["profesion"] = "Ingeniero"
print("Persona con profesion:", persona)

print("Claves", persona.keys()) #claves
print("Valores", persona.values())  #valores

persona["ciudad"] = "Quito"
print("Ciudad modificada", persona)