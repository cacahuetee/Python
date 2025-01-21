#ejercicio 1
numero = 0
while numero <= 10:
    print(numero)
    numero += 1

#ejercicio 2
suma = 0
while True:
        num = int(input("Introduce un número: "))
        if num == 0:
            break
        suma += num
print(f"La suma de los números ingresados es: {suma}")

#ejercicio 3
numero1 = 5
factorial = 1
contador = numero1
while contador > 0:
    factorial *= contador
    contador -= 1
print(f"El factorial de {numero1} es: {factorial}") 
    