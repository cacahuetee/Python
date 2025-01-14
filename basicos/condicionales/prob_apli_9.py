temp = int(input("Introduce una temperatura en grados Celsius: "))

if temp >= 30:
    print(f"Hace calor, hay {temp} grados")
elif 10 <= temp <= 29:
    print(f"El clima es templado, hay {temp} grados")
else:
    print(f"Hace frío, hay {temp} grados")