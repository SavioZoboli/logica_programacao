print("|-----------------------|")
print("|      Calculadora      |")
print("|-----------------------|")
print()
print("Essa calculadora, faz todas as operações")
print("a partir de dois números que você informar")
print()

print("Digite o valor correspondente ao cálculo")
print("que você quer fazer")
print()
print("1 - As 4 operações")
print("2 - Média de 3 valores")
print("3 - Fórmula de Bháskara")
print()
opcao = int(input("Digite a opção: "))

match opcao:
    case 1:
        first_num = float(input("Digite o primeiro numero: "))
        second_num = float(input("Digite o segundo número: "))
        print()

        adicao = first_num + second_num
        print("A adição resulta em:",adicao)

        subtracao = first_num - second_num
        print("A subtração resulta em:",subtracao)

        multi = first_num * second_num
        print(f"A multipliacação resulta em {multi}")

        # Verificando se o segundo número é diferente de 0
        if second_num != 0:
            divisao = first_num / second_num
            print(f"A divisão resulta em {divisao}")
        else:
            print("A divisão não pode ser feita.")

    case 2:
        print("Média de 3 valores")
        primeiro_valor = float(input("Digite o primeiro valor: "))
        segundo_valor = float(input("Digite o segundo valor: "))
        terceiro_valor = float(input("Digite o terceiro valor: "))

        media = (primeiro_valor + segundo_valor + terceiro_valor) / 3

        print(f"A média dos valores é: {media}")

    case 3:
        print("Fórmula de Bháskara")




print()