def calculadora():
    while True:
        print("\nEscolha a operação:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")
        
        operacao = input("Digite o número da operação desejada: ")
        
        if operacao == '0':
            print("Saindo...")
            break
        elif operacao in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                
                if operacao == '1':
                    resultado = num1 + num2
                    print(f"Resultado da soma: {resultado}")
                elif operacao == '2':
                    resultado = num1 - num2
                    print(f"Resultado da subtração: {resultado}")
                elif operacao == '3':
                    resultado = num1 * num2
                    print(f"Resultado da multiplicação: {resultado}")
                elif operacao == '4':
                    if num2 != 0:
                        resultado = num1 / num2
                        print(f"Resultado da divisão: {resultado}")
                    else:
                        print("Erro: Divisão por zero não é permitida.")
            except ValueError:
                print("Entrada inválida. Por favor, digite números válidos.")
        else:
            print("Essa opção não existe. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    calculadora()