"""
Aluno: Estevão Batista de Moraes
Este documento contém o Exercício 1 e o Exercício 2 da AC de Programação Estruturada.

Objetivo do Exercício 1: elaborar um código em Python que resolva uma equação do segundo
grau, cujos parâmetros devem ser entregues pelo usuário.

Objetivo do Exercício 2: elaborar um código em Python que receba o valor de um ano e em
seguida verifique se ele é bissexto ou não.
"""
#Exercício 1
a = float(input("Informe o parâmetro a da equação: "))
b = float(input("Informe o parâmetro b da equação: "))
c = float(input("Informe o parâmetro c da equação: "))

delta = b**2 - 4*a*c
primeira_raiz = (-b+delta**0.5)/(2*a)
segunda_raiz = (-b-delta**0.5)/(2*a)

print("A primeira raiz da equação é", primeira_raiz)
print("A segunda raiz da equação é", segunda_raiz, end="\n\n")

#Exercício 2
ano = int(input("Informe o ano: "))
print(ano%100!=0 and ano%4==0 or ano%100==0 and ano%400==0)