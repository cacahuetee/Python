def es_par():
    num = int(input("Introduce un número: "))
    return num % 2 == 0

if es_par():
    print("El número es par.")
else:
    print("El número es impar.")