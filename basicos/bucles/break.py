import getpass
import random
#ejercicio 1
contrasena_correcta = "python123"
while True:
    contrasena = getpass.getpass("Introduce la contraseña: ")
    if contrasena == contrasena_correcta:
        break
print("Bienvenido usuario")

#ejercicio 2
while True:
    numero = random.randint(1,10)
    print(f"Generado: {numero}")
    if numero > 8:
        break
print("Se ha generado un número myor que 8, se ha salido del bucle")

#ejercicio 3
secreto = random.randint(1,20)
while True:
    adivina = input("Introduce un número para intentar adivinar el secreto: ")
    if adivina.lower() == "salir":
        print(f"Has abandonado el juego, el número secreto era: {secreto}")
        break
    if adivina.isdigit():
        adivina = int(adivina)
        if adivina == secreto:
            print(f"Has adivinado el número secreto {secreto}")
            break