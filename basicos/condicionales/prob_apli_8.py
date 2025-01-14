import getpass

contraseña = getpass.getpass("Introduce la contraseña: ")

if contraseña == "secreto123":
    print("Acceso concedido.")
else:
    print("Acceso denegado. Contraseña incorrecta")
