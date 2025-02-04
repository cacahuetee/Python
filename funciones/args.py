def promedio(*args):
    if len(args) == 0:
        print("No se han introducido números.")
        return None
    return sum(args) / len(args)

def pedir_numeros():
    cantidad = int(input("¿Cuántos números quieres ingresar para calcular el promedio? "))
    numeros = []
    for i in range(cantidad):
        numero = float(input(f"Introduce el número {i+1}: "))
        numeros.append(numero)
    return numeros

numeros = pedir_numeros()
resultado = promedio(*numeros)

if resultado is not None:
    print(f"El promedio de los números ingresados es: {resultado}")
