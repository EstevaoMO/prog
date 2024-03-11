"""
Aluno: Estevão Batista de Moraes
11.03.2024 | Aula de Programação Estruturada

Este documento contém a AC4 de Programação Estruturada
"""

def ler_nome():
    """ Retorna o nome do aluno. """
    return input("Informe o seu nome: ")

def ler_notas():
    """ Lê as quatro notas das avaliações e retorna os valores. """
    ap1 = float(input("Informe sua nota da AP1: "))
    ap2 = float(input("Informe sua nota da AP2: "))
    asub = float(input("Informe sua nota da AS: "))
    ac = float(input("Informe sua nota da AC: "))
    return ap1, ap2, asub, ac


def notas_sao_validas(ap1, ap2, asub, ac):
    """
    Retorna True se as quatro notas estão entre 0 a 10.
    Retorna False caso contrário.
    """
    return (ap1 >= 0 and ap1 <= 10) and (ap2 >= 0 and ap2 <= 10) and (asub >= 0 and asub <= 10) and (ac >= 0 and ac <= 10)

def duas_maiores_notas(ap1, ap2, asub):
    """
    Retorna as duas maiores notas dentre as avaliações apresentadas.
    Substitui a AP1 pela AS caso AS > AP1
    Substitui a AP2 pela AS caso AS > AP2
    A AS só substitui uma das duas provas (a menor delas).
    Caso a AS seja menor que a AP1 e a AP2, retorna AP1 e AP2.
    """
    if ap1 < ap2 and asub > ap1:
        return asub, ap2
    if ap2 < ap1 and asub > ap2:
        return ap1, asub
    else:
        return ap1, ap2

def calcular_media(nota1, nota2, ac):
    """
    Retorna a média das avaliações, arredondando para duas casas decimais.
    M = (NOTA1 + NOTA2) * 0.4 + AC * 0.2
    """
    return round((nota1 + nota2) * 0.4 + ac * 0.2, 2)

def aluno_foi_aprovado(media):
    """
    Retorna True caso a média seja maior ou igual a 7.
    Retorna False caso contrário.
    """
    return media >= 7

def main():
    nome = ler_nome()
    if nome:
        ap1, ap2, asub, ac = ler_notas()
        if notas_sao_validas(ap1, ap2, asub, ac):
            prova1, prova2 =  duas_maiores_notas(ap1, ap2, asub)
            media = calcular_media(prova1, prova2, ac)
            if aluno_foi_aprovado(media):
                print("Aluno foi aprovado!")
            else:
                print("Aluno foi reprovado!")

main()
