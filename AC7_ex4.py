def recebe_valor():
    while True:
        valor = int(input())
        if valor <= 50:
            return valor
        else:
            print("Valor impróprio!")

def vetor_dobrando(vetor, valor_inicial):
    dobro = valor_inicial

    for _ in range(10):
        vetor.append(dobro)
        dobro *= 2

    return vetor

def display_vetor(vetor):
    for componente in range(10):
        print(f"N[{componente}] = {vetor[componente]}")

def main():
    valor_inicial = recebe_valor()

    vetor = []
    vetor = vetor_dobrando(vetor, valor_inicial)

    display_vetor(vetor)

if __name__ == "__main__":
    main()