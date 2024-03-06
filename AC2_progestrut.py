"""
Aluno: Estevão Batista de Moraes
Este documento contém o Exercício 1 e o Exercício 2 da AC2 de Programação Estruturada.

Objetivo do Exercício 1: desenvolver uma função que calcule uma função de segundo grau.

Objetivo do Exercício 2: desenvolver uma função que calcule o salário de um indivíduo.
de renda dado.
"""
#Exercício 1
def eq_seg_grau(a, b, c):
    delta = b**2 - 4*a*c
    primeira_raiz = (-b+delta**0.5)/(2*a)
    segunda_raiz = (-b-delta**0.5)/(2*a)
    return primeira_raiz, segunda_raiz

def verifica_bissexto(ano):
    return ano%100!=0 and ano%4==0 or ano%400==0

#Exercício 2
def calcula_salario(valor_hora, num_horas, irpf):
    return valor_hora*num_horas - valor_hora*num_horas*irpf

#Código principal
def main():
    print(eq_seg_grau(1, -6, 8))
    print(eq_seg_grau(2, 16, 3))
    print(verifica_bissexto(1900))
    print(verifica_bissexto(1984))
    print(calcula_salario(9, 145, 0.215))
    print(calcula_salario(8.825, 160, 0.215))

main()