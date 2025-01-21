#ejercicio 1
cadena1 = "Python es genial"
vocales = "aeiouAEIOU"
contador = 0
for char in cadena1:
    if char in vocales:
        contador += 1

print(contador)

#ejercicio 2
cadena2 = "Hola Mundo"
invertida = ""
for char in cadena2:
    invertida = char + invertida

print(invertida)

#ejercicio 3
cadena3 = "Hola a todos"
sin_epacios = ""
for char in cadena3:
    if char != " ":
        sin_epacios += char

print(sin_epacios)