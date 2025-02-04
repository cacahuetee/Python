def saludo_personalizado():
    nombre = input("Introduce tu nombre: ")
    edad = int(input("Introduce tu edad: "))
    print(f"Hola, {nombre}. Tienes {edad} años.")

    saludo_personalizado()