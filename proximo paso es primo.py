def es_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def next_prime(n):
    numero = n + 1
    while True:
        if es_primo(numero):
            return numero
        numero += 1

def main():
    n = int(input("Ingrese un número entero: "))
    siguiente_primo = next_prime(n)
    print(f"El primer número primo mayor que {n} es {siguiente_primo}.")

if __name__ == "__main__":
    main()