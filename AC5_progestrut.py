from random import randint

def main():
    #Informações do Aventureiro
    vida_aventureiro = 100
    ataque_aventureiro = randint(10, 20)
    defesa_aventureiro = randint(1, 5)

    #Informações do Monstro
    vida_monstro = randint(60, 80)
    ataque_monstro = randint(20, 30)

    #Exibição dos Atributos Iniciais
    print(f"""
Aventureiro
{vida_aventureiro} de vida;
{ataque_aventureiro} de ataque;
{defesa_aventureiro} de defesa.""", end="\n")
    print(f"""
Monstro
{vida_monstro} de vida;
{ataque_monstro} de ataque;
0 de defesa.\n""")

    #Loop de Rodadas
    rodada = 1
    while True:
        print(f"{"="*10}Rodada {rodada}", "="*10, sep="")
        ataque_monstro_rodada = randint(1, ataque_monstro) - defesa_aventureiro
        if  ataque_monstro_rodada < 0:
            ataque_monstro_rodada = 0
        vida_aventureiro -= ataque_monstro_rodada
        vida_monstro -= randint(1, ataque_aventureiro)

        if vida_aventureiro <= 0:
            print("O aventureiro morreu!\n")
            break
        elif vida_monstro <= 0:
            print("O monstro morreu!\n")
            break
        else:
            rodada += 1

        print(f"Aventureiro: vida {vida_aventureiro} - att {ataque_aventureiro} - def {defesa_aventureiro}")
        print(f"Monstro: vida {vida_monstro} - att {ataque_monstro}")

main()