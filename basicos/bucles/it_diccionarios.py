#ejercicio 1
productos = {"manzana": 1.5, "banana": 0.8, "leche": 2.3}
for producto, precio in productos.items():
    print(f"{producto}: ${precio:.2f}") #:.2f redondea a dos decimales

#ejercicio 2
precios = sum(productos.values())
print("Precios totales: ", precios)

#ejercicio 3
#valor = 1.0
#caros = [articulo for nombre, precio in productos.items() if precio > valor]
#print(caros)

valor = 1.0
caros = []
for producto, precio in productos.items():
    if precio > valor:
        caros.add(producto) 

print(caros)
