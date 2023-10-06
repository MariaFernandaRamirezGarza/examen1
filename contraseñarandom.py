import random

def generar_contrasena():
    longitud = random.randint(7, 10)
    contrasena = ""
    for _ in range(longitud):
        caracter = chr(random.randint(33, 126))
        contrasena += caracter
    return contrasena

if __name__ == "__main__":
    contrasena_generada = generar_contrasena()
    print(f"Contraseña generada: {contrasena_generada}")
