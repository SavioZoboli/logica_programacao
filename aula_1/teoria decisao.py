# Nesse código, analisaremos a idade do usuário e falaremos
# se é maior de idade ou não
nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))

print("Olá, ",nome,"! A sua idade é ",idade)

# A estrutura de decisão analisa uma comparação e executa o código
# com base na resposta. Para utilizarmos a estrutura de decisão, precisamos
# de comparadores, que são:

# - > maior
# - < menor
# - == igual
# - != diferente
# - >= maior ou igual
# - <= menor ou igual
# - ! não

# O comando de decisão é o if
# A sintaxe é: 
# if comparacao :
# E os itens a serem executados devem estar em um bloco identado.
# if 20 > 30:
#   print("Algo de errado não está certo")

if idade >= 18:
    print("Você é maior de idade!")
    if idade >= 60:
        print("Você é idoso!")
        print("Já pode pegar a carteirinha de estacionamento")
else:
    print("Você é menor de idade!")
    print("Não pode comprar cigarro no Reino Unido")