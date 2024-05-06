""" Prime stuff, i mean, numbers :) """
num_casos = int(input())

for _ in range(num_casos):
    valor_lido = int(input())
    raiz_valorlido = int(valor_lido**0.5)
    primo = "Prime"

    for numero in range(2, raiz_valorlido+1):
        if valor_lido % numero == 0:
            primo = "Not Prime"
            break

    if valor_lido == 1:
        primo = "Not Prime"

    print(primo)

""" Cara ou coroa :) """

def conta_vitorias(jogos : list):
    vitorias_maria = 0
    vitorias_joao = 0

    for jogo in jogos:
        if jogo == "0":
            vitorias_maria += 1
        elif jogo == "1":
            vitorias_joao += 1
        else:
            print("Item Inválido! Apenas 0's e 1's são passíveis de análise!")

    print(f"Mary won {vitorias_maria} times and John won {vitorias_joao} times")

def main():
    while True:

        numero_jogos = int(input())
        if numero_jogos == 0:
            break

        jogos = input().split()
        conta_vitorias(jogos)


if __name__ == "__main__":
    main()

"""
A função que Rafael escolheu é r(x, y) = (3x)² + y².

Já Beto escolheu a função b(x, y) = 2(x²) + (5y)².

Carlos, por sua vez, escolheu a função c(x, y) = -100x + y³.
"""

def funcao_rafael(x : int, y : int):
    return ((3*x)**2) + (y**2)

def funcao_beto(x : int, y : int):
    return (2*(x**2)) + ((5*y)**2)

def funcao_carlos(x : int, y : int):
    return (-100*x) + (y**3)

def main():
    numero_casos = int(input())

    for _ in range(numero_casos):
        x, y = input().split()
        x = int(x); y = int(y)

        if funcao_rafael(x, y) > funcao_beto(x, y) and funcao_rafael(x, y) > funcao_carlos(x, y):
            print("Rafael ganhou")
        elif funcao_beto(x, y) > funcao_rafael(x, y) and funcao_beto(x, y) > funcao_carlos(x, y):
            print("Beto ganhou")
        elif funcao_carlos(x, y) > funcao_rafael(x, y) and funcao_carlos(x, y) > funcao_beto(x, y):
            print("Carlos ganhou")

if __name__ == "__main__":
    main()

""" Soma dos Fatoriais... yey :) """

def fatorial(numero : int):
    fatorial = 1

    for valor in range(1, numero+1):
        fatorial *= valor

    return fatorial

def main():
    while True:
        try:
            m, n = input().split()
            m, n = int(m), int(n)

        except ValueError:
            break

        except EOFError:
            break

        soma_fatoriais = fatorial(m) + fatorial(n)

        print(soma_fatoriais)


if __name__ == "__main__":
    main()

""" Lista doida dos números repetidos :) """
numero_casos = int(input())

valores = []
for _ in range(numero_casos):
    valores.append(int(input()))

sem_repetidos = list(set(valores))
sem_repetidos.sort()

for i in range(len(sem_repetidos)):
    print(f"{sem_repetidos[i]} aparece {valores.count(sem_repetidos[i])} vez(es)")

""" Blobs :) """

num_casos = int(input())

for _ in range(num_casos):
    quantidade_comida = float(input())

    quantidade_dias = 0

    while quantidade_comida > 1:
        quantidade_comida /= 2
        quantidade_dias += 1

    print(f"{quantidade_dias} dias")

""" Figurinhas :) """
from math import gcd

num_casos = int(input())

for _ in range(num_casos):
    pilha1, pilha2 = input().split()
    pilha1, pilha2 = int(pilha1), int(pilha2)

    print(gcd(pilha1, pilha2))

""" O da dama não deu tempo de fazer :( """