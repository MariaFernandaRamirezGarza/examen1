def es_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False

num = int(input("Ingrese un número: "))
mensaje = "es primo" if es_primo(num) else "no es primo"
print(f"{num} {mensaje}.")
