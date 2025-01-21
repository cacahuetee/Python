#ejercicio 1
numeros = {1,2,3}
numeros.add(4)
print(numeros)

#ejercicio 2
print(5 in numeros)

#ejercicio 3
conjunto1 = {1,2,3}
conjunto2 = {2,3,4}
interseccion = conjunto1.intersection(conjunto2)
print(interseccion)

#otra manera del 3
suma = conjunto1|conjunto2
#suma = conjunto1.union(conjunto2)
print(suma)

