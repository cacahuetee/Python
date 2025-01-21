#ejercicio 1
numeros = [1,2,3,4,5]
suma = sum(numeros)
print(suma)

#ejercicio 2
nombres = ["ana", "luis", "carlos"]
mayusculas = [nombre.upper() for nombre in nombres]
capital = [nombre.capitalize() for nombre in nombres]
print(mayusculas)
print(capital)

#ejercicio 3
numeros = [10,15,20,25,30]
pares = [num for num in numeros if num % 2 == 0]
#for num in numeros:
    #if num % 2 == 0:
        #numeros_pares.append(num)
print(pares)