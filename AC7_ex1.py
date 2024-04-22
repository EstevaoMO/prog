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