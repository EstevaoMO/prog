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