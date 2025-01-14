numero = int(input("Introduce un número del 1 al 7: "))

if numero >= 1 and numero <=7:
    if numero == 1:
        print(f"{numero}:Lunes")
    elif numero == 2:
        print(f"{numero}:Martes")
    elif numero == 3:
        print(f"{numero}:Miércoles")
    elif numero == 4:
        print(f"{numero}:Jueves")
    elif numero == 5:
        print(f"{numero}:Viernes")
    elif numero == 6:
        print(f"{numero}:Sábado")
    else:
        print(f"{numero}:Domingo")
else:
    print("Asegúrate de introducir un número del 1 al 7")