letra = input("Introduce una letra minúscula: ")

if len(letra) == 1 and letra.islower() and letra.isalpha():
    
    if letra in 'aeiou':
        print(f"La letra {letra} es una vocal.")
    else:
        print(f"La letra {letra} es una consonante.")
else:
    print("Por favor, introduce una sola letra minúscula.")