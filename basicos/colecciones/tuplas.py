import random
#ejercicio 1
ciudades = ("Madrid", "Roma", "París")
print(ciudades)

#ejercicio 2
numeros = (100, 200, 300)
print(numeros[1])

#ejercicio 3
tupla = ()
nuevo = random.randint(1, 100)
tupla_modificada = tupla + (nuevo,)
print("Tupla original:", tupla)
print("Tupla modificada:", tupla_modificada)