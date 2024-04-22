def le_tamanho():
    return int(input())

def le_valores():
    valores = input().split()

    return valores

def menor_valor(lista : list):
    menor_valor = int(lista[0])

    for item in range(len(lista)):
        lista[item] = int(lista[item])

        if lista[item] < menor_valor:
            menor_valor = lista[item]

    return menor_valor

def pos_menor_valor(lista : list):
    menor_valor = int(lista[0])

    for item in range(len(lista)):
        lista[item] = int(lista[item])

        if lista[item] < menor_valor:
            menor_valor = lista[item]

    pos = lista.index(menor_valor)
    return pos

def main():
    tamanho_vetor = le_tamanho()

    vetor = le_valores()
    menor_valor_vetor = menor_valor(vetor)
    posicao_menor_valor = pos_menor_valor(vetor)

    print(f"Menor valor: {menor_valor_vetor}")
    print(f"Posicao: {posicao_menor_valor}")


if __name__ == "__main__":
    main()