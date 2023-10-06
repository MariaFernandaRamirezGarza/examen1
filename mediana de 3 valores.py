def mediana_de_tres(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort()
    return numeros[1]

def main():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    num3 = float(input("Ingrese el tercer número: "))
    
    mediana = mediana_de_tres(num1, num2, num3)
    print(f"La mediana de los números ingresados es: {mediana}")

if __name__ == "__main__":
    main()

