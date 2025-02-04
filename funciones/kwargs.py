def imprimir_detalles(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

imprimir_detalles(nombre="Carlos", edad=25, ciudad="Madrid")
print()  
imprimir_detalles(marca="Toyota", modelo="Corolla", año=2020, color="Rojo")
print()
imprimir_detalles(nombre="Ana", ocupacion="Ingeniera", pais="España")
print()