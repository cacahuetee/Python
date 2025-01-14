precio = float(input("Introduce el precio del producto: "))

if precio > 1000:
    precio_final = precio * 0.90
    print(f"Se aplica un descuento del 10%. El precio final es: {precio_final:.2f}")
else:
    print(f"El precio del producto es: {precio:.2f}")