def le_coluna():
    coluna = int(input())

    return coluna

def le_operacao():
    operacao = input().upper()

    return operacao

def le_matriz():
    matriz = []

    for i in range(12):
        matriz.append([])

        for _ in range(12):
            valor_linha = float(input())
            matriz[i].append(valor_linha)

    return matriz

def operacao_matriz(matriz : list, operacao : str, coluna_de_operacao : int):
    resultado = 0

    if operacao == "S":

        for i in range(len(matriz)):
            resultado += matriz[i][coluna_de_operacao]


    elif operacao == "M":
        qntd_valores = len(matriz)

        for i in range(len(matriz)):
            resultado += matriz[i][coluna_de_operacao]

        resultado /= qntd_valores

    return resultado

def main():
    coluna_de_operacao = le_coluna()
    operacao = le_operacao()
    matriz = le_matriz()

    print(f"{operacao_matriz(matriz, operacao, coluna_de_operacao):.1f}")

if __name__ == "__main__":
    main()