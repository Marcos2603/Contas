def obter_nome():
    return input("Digite seu nome completo: ")

def obter_ano_nascimento():
    while True:
        try:
            ano_nascimento = int(input("Digite seu ano de nascimento (entre 1922 e 2021): "))
            if 1922 <= ano_nascimento <= 2021:
                return ano_nascimento
            else:
                print("Ano inválido. Por favor, digite um ano entre 1922 e 2021.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")

def calcular_idade(ano_nascimento):
    ano_atual = 2022
    return ano_atual - ano_nascimento

def main():
    nome = obter_nome()
    ano_nascimento = obter_ano_nascimento()
    idade = calcular_idade(ano_nascimento)
    print(f"{nome}, você completou ou completará {idade} anos em 2022.")

if __name__ == "__main__":
    main()
