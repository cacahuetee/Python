def saludar_con_titulo():
    nombre = input("Introduce tu nombre: ")
    titulo = input("Introduce tu título (opcional, presiona Enter para omitir): ")
    if not titulo:
        titulo = "Sr./Sra." 
    print(f"Hola, {titulo} {nombre}.")

    saludar_con_titulo()