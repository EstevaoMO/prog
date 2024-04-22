def recebe_cinco_numeros():
    numeros = []
    for _ in range(5):
        numero = int(input())
        numeros.append(numero)

    return numeros

def quantos_pares_dentre(numeros):
    quantidade_pares = 0

    for numero in numeros:
        if numero % 2 == 0:
            quantidade_pares += 1

    return quantidade_pares

def main():
    numeros = recebe_cinco_numeros()
    print(f"{quantos_pares_dentre(numeros)} valores pares")

if __name__ == "__main__":
    main()