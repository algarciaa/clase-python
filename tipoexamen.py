#ingreso y validacion de la cantidad de productos
num_tipos_producto = 0
entrada_valida = False

while not entrada_valida:
    try:
        entrada = input("Ingrese la cantidad de tipos de productos a registrar:")
        num_tipos_producto = int(entrada)

        if num_tipos_producto > 0:
            entrada_valida = True
        else:
            print("Error: Ingrese un numero entero positivo para la cantidad de productos")
    except ValueError:
        print("Error: Ingrese un numero entero valido")

#inicializar las listas
nombres_productos = []
stocks = []

#variables de analisis
stock_bajo = 0
stock_normal = 0

print(f"Registrar {num_tipos_producto} productos")

#ciclo for para registrar los productos
for i in range(num_tipos_producto):
    nombre = ""

    while not nombre:
        print(f"Producto #[{i + 1}]")

        nombre = input("Ingrese nombre del producto").strip()

        if not nombre:
            print("Error: el nombre del producto no puede estar vacio")

        nombres_productos.append(nombre)

    stock_valido = False

    while not stock_valido:
        try:
            entrada_stock = input("Ingrese stock inicial")
            stock = int(entrada_stock)

            if stock > 0:
                stock_valido = True
                stocks.append(stock)

                if stock <= 5:
                    stock_bajo += 1
                else:
                    stock_normal += 1
            else:
                print("El stock no debe ser negativo")

        except ValueError:
            print("Error: Ingrese un numero entero valido para el stock")

producto_mayor_stock = "NA"
stock_maximo = 0

if stocks:
    stock_maximo = max(stocks)

    indice_maximo = stocks.index(stock_maximo)
    producto_mayor_stock = nombres_productos[indice_maximo]

for i in range(len(nombres_productos)):
    print(f"{nombres_productos[i]} - {stocks[i]} unidades")

print(f"Total tipo productos: {num_tipos_producto}")
print(f"producto stock bajo: {stock_bajo}")
print(f"producto stock normal: {stock_normal}")
print(f"producto con mayor stock: {stock_maximo}")