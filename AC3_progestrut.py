"""
Aluno: Estevão Batista de Moraes
Este documento contém o Exercício 1, Exercício 2 e Exercício 3 da AC3 de Programação Estruturada.

Exercício 1: Desenvolva uma função determina_tipo_triangulo que recebe três
lados de um triângulo e retorna uma string, "Escaleno", "Isósceles" ou "Equilátero",
conforme o tipo do triângulo. A função deve retornar "Não é um triângulo" se os três
lados não formarem um triângulo.

Exercício 2: Desenvolva uma função dia_semana que recebe um número inteiro e
retorna uma string indicando o dia da semana equivalente, considerando que o dia da semana
igual a 1 é o domingo, 2 é segunda-feira, etc. A função deve retornar uma string vazia caso
o número seja inválido.

Exercício 3: Desenvolva funções de operações aritméticas soma, subtracao, multiplicacao
e divisao, que recebem dois números cada uma e retornam o resultado da operação indicada. Em seguida,
crie uma função que elabora uma interface por linha de comando (CLI), que lê dois números e uma operação
e exibe na tela o valor do resultado, ou exibe "operação inválida" se o usuário inserir uma mensagem
diferente das quatro operações.
"""
#Exercício 1
def qual_tipo_triangulo(lado1, lado2, lado3):
    if lado1 < lado2+lado3 and lado2 < lado1+lado3 and lado3 < lado2+lado1:
        if lado1 == lado2 == lado3:
            return "Equilátero"
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            return "Isósceles"
        else:
            return "Escaleno"
    else:
        return "Não é um triângulo"

#Exercício 2
def dia_semana(numero):
    match numero:
        case 1:
            return "Domingo"
        case 2:
            return "Segunda-feira"
        case 3:
            return "Terça-feira"
        case 4:
            return "Quarta-feira"
        case 5:
            return "Quinta-feira"
        case 6:
            return "Sexta-feira"
        case 7:
            return "Sábado"
        case _:
            return ""

#Exercício 3
def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    return num1 / num2

def interface_calculadora():
    valor1 = int(input("Informe um número: "))
    valor2 = int(input("Informe outro número: "))
    operacao = input("Informe a operação: ").lower()
    match operacao:
        case "soma":
            print(f"Resultado: {soma(valor1, valor2)}")
        case "subtração":
            print(f"Resultado: {subtracao(valor1, valor2)}")
        case "multiplicação":
            print(f"Resultado: {multiplicacao(valor1, valor2)}")
        case "divisão":
            print(f"Resultado: {divisao(valor1, valor2)}")
        case _:
            print("Operação Inválida")

def main():
    print(qual_tipo_triangulo(2, 3, 4))
    print(qual_tipo_triangulo(2, 4, 4))
    print(qual_tipo_triangulo(4, 4, 4))
    print(qual_tipo_triangulo(1, 2, 4))

    print(dia_semana(4))
    print(dia_semana(6))
    print(dia_semana(9))

    interface_calculadora()

main()