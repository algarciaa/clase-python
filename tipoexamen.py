print("--- GESTOR DE INVENTARIO BÁSICO (PYTHON) ---")

# 1. Ingreso y Validación de la cantidad de productos
num_tipos_producto = 0
entrada_valida = False

while not entrada_valida:
    try:
        entrada = input("\nIngrese la cantidad de tipos de productos a registrar: ")
        num_tipos_producto = int(entrada)
        
        # Validación IF: si es positivo
        if num_tipos_producto > 0:
            entrada_valida = True
        else:
            print("ERROR: Ingrese un número entero positivo para la cantidad de productos.")
    except ValueError:
        print("ERROR: Ingrese un número entero válido.")

# 2. Inicializar las Listas
# NOTA: En Python, a menudo se usa un diccionario para combinar nombre y stock, 
# pero para mantener la estructura de Listas paralelas del ejercicio C#, se usan dos.
nombres_productos = []
stocks = []

# Variables para el análisis
stock_bajo = 0
stock_normal = 0

print(f"\n--- REGISTRANDO {num_tipos_producto} PRODUCTOS ---")

# 3. Ciclo FOR para registrar Nombres y Stocks
for i in range(num_tipos_producto):
    nombre = ""
    
    # --- Ingreso y validación del Nombre (Ciclo while) ---
    while not nombre: # Es equivalente a 'while nombre == ""' o 'while string.IsNullOrEmpty(nombre)'
        print(f"\n[Producto #{i + 1}]")
        nombre = input("Ingrese el nombre: ").strip() # .strip() equivale a .Trim() en C#
        
        # Validación IF: Nombre no vacío
        if not nombre:
            print("!!! ALERTA: El nombre del producto no puede estar vacío.")

    nombres_productos.append(nombre) # Agrega el nombre a la lista

    # --- Ingreso y validación del Stock (Ciclo while y try-except) ---
    stock_valido = False
    while not stock_valido:
        try:
            entrada_stock = input(f"[Producto #{i + 1}] Ingrese el stock inicial: ")
            stock = int(entrada_stock)
            
            # Validación IF: Stock no negativo
            if stock >= 0:
                stock_valido = True
                stocks.append(stock) # Agrega el stock a la lista
                
                # 4. Análisis de Stock (IF)
                if stock <= 5:
                    stock_bajo += 1
                else: # stock > 5
                    stock_normal += 1
            else:
                print("!!! ALERTA: El stock no puede ser negativo. Intente de nuevo.")
        
        except ValueError:
            print("!!! ALERTA: Ingrese un número entero válido para el stock.")

# 5. Análisis adicional: Encontrar el producto con mayor stock
producto_mayor_stock = "N/A"
stock_maximo = 0

# Verifica que la lista no esté vacía
if stocks: # Es equivalente a 'if stocks.Count > 0'
    stock_maximo = max(stocks) # La función max() de Python
    
    # Encontrar el índice del stock máximo
    # NOTA: Si hay stocks repetidos, index() devuelve el índice del primero que encuentra.
    indice_maximo = stocks.index(stock_maximo) 
    producto_mayor_stock = nombres_productos[indice_maximo] 

# 6. Mostrar Resumen Final
print("\n=============================================")
print("           RESUMEN DE INVENTARIO             ")
print("=============================================")

# Muestra el inventario completo (usando el FOR con range() para iterar ambas listas)
print("\n--- INVENTARIO DETALLADO ---")
for i in range(len(nombres_productos)):
    print(f"- {nombres_productos[i]}: {stocks[i]} unidades.")

print("\n--- ANÁLISIS ---")
print(f"Total de Tipos de Productos: {num_tipos_producto}")
print(f"Productos en Stock Bajo (<= 5): {stock_bajo} tipos.")
print(f"Productos en Stock Normal (> 5): {stock_normal} tipos.")
print("---------------------------------------------")
print(f"Producto con mayor stock ({stock_maximo} uds.): {producto_mayor_stock}")
print("=============================================")
