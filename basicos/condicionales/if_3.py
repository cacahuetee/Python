import random

numero = random.randint(-10, 10)

print(f"Número generado: {numero}")

if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es igual a 0.")