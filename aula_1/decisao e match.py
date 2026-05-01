temp = -5

if temp > 25:
    print("Está calor")
elif temp > 15:
    print("Está agradável")
elif temp > 5:
    print("Está frio")
else:
    print("Está congelando")

print("Com base na temperatura acima, o que deseja fazer?")
print("1 - Ligar o aquecedor")
print("2 - Ligar o ar-condicionado")

opcao = input("Escolha uma opção:")

match opcao:
    case "1":
        print("Ligando o aquecedor, logo ficará quentinho.")
    case "2":
        print("Ligando o ar-condicionado, logo ficará frio")
    case _:
        print("Comando inválido")


print("Fim da execução.")
