#EXERCÍCIO 1
def recebe_salario():
    salario = float(input())

    return salario

def aumenta_salario(salario):
    if 0 <= salario <= 400:
        novo_salario = (0.15 * salario) + salario
    elif 400 < salario <= 800:
        novo_salario = (0.12 * salario) + salario
    elif 800 < salario <= 1200:
        novo_salario = (0.10 * salario) + salario
    elif 1200 < salario <= 2000:
        novo_salario = (0.07 * salario) + salario
    elif 2000 < salario:
        novo_salario = (0.04 * salario) + salario
    else:
        return "Salário inválido!"

    return novo_salario

def percentual_de_aumento(salario):
    if 0 <= salario <= 400:
        return "15 %"
    elif 400 < salario <= 800:
        return "12 %"
    elif 800 < salario <= 1200:
        return "10 %"
    elif 1200 < salario <= 2000:
        return "7 %"
    elif 2000 < salario:
        return"4 %"
    else:
        return "Salário inválido!"

def valor_reajuste(salario_antigo, novo_salario):
    return novo_salario - salario_antigo

def display_salario(salario_antigo, novo_salario):
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {valor_reajuste(salario_antigo, novo_salario):.2f}")
    print(f"Em percentual: {percentual_de_aumento(salario_antigo)}")

def main():
    salario_usuario = recebe_salario()
    novo_salario_usuario = aumenta_salario(salario_usuario)
    display_salario(salario_usuario, novo_salario_usuario)

if __name__ == "__main__":
    main()



#EXERCÍCIO 2
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



#EXERCÍCIO 3
def recebe_dois_inteiros():
    primeiro_inteiro = int(input())
    segundo_inteiro = int(input())

    return primeiro_inteiro, segundo_inteiro

def soma_nao_multiplos_entre(valor_inicial, valor_final, numero_para_dividir):
    soma = 0

    valores = [valor_inicial, valor_final]
    if valor_inicial > valor_final:
        valor_final = valores[0]
        valor_inicial = valores[1]

    for numero in range(valor_inicial, valor_final+1):
        if numero % numero_para_dividir != 0:
            soma += numero

    return soma

def main():
    primeiro_valor, segundo_valor = recebe_dois_inteiros()
    print(soma_nao_multiplos_entre(primeiro_valor, segundo_valor, 13))

if __name__ == "__main__":
    main()



#EXERCÍCIO 4
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



#EXERCÍCIO 5
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



#EXERCÍCIO 6
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