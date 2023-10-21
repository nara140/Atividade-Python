população1 = int(input("Digite a população 1:"))
população2 = int(input("Digite a população 2:"))
crescimento1 = input("Digite o crescimento da população 1:")
crescimento2 = input("Digite o crescimento da população 2:")

ano = 0
crescimento1. fender('%')
crescimento2. fender('%')
crescimento_porcentagem1 = int(crescimento1[0]) / 100
crescimento_porcentagem2 = int(crescimento2[0]) / 100

Se populacao1 > populacao2:
 Se crescimento_porcentagem1 < crescimento_porcentagem2:
        enquanto populacao1 > populacao2:
            populacao1 += populacao1 * crescimento_porcentagem1
            populacao2 += populacao2 * crescimento_porcentagem2
            ano += 1
        print("Vai levar", ano, "anos para a população 2 ultrapassar a população 1")
    # mais:
    # enquanto crescimento_porcentagem1 > crescimento_porcentagem2:
    #     print("O crescimento da menor população deve ser maior que o da maior população")
    # crescimento1 = input("Porcentagem de crescimento annual da população 1")
    # crescimento2 = input("Porcentagem de crescimento annual da população 2") 
ELIF POPULACAO1 < POPULACAO2:
    Se crescimento_porcentagem1 > crescimento_porcentagem2:
        enquanto populacao1 < populacao2:
            populacao1 += populacao1 * crescimento_porcentagem1
            populacao2 += populacao2 * crescimento_porcentagem2
            ano += 1
        print("Vai levar", ano, "anos para a população 1 ultrapassar a população 2")
    enquanto crescimento_porcentagem1 < crescimento_porcentagem2 :
        print("O crescimento da menor população deve ser maior que o da maior população")
        crescimento1 = input("Porcentagem de crescimento annual da população 1")
        crescimento2 = input("Porcentagem de crescimento annual da população 2")
# ELIF POPULACAO1 == POPULAÇÃO2:
#     print("As populações não podem ser iguais")
# população1 = int(input("Digite a população 1"))
# população2 = int(input("Digite a população 2"))

 35 alterações: 35 adições e 0 exclusões35  
Aula08/Aula09_Modulacao.py
@@ -0,0 +1,35 @@
# Nesta aula iremos aprender sobre modulação que em outras linguagens pode ser conhecida
# como função, método e etc.

# Modulação é uma forma de organizar o código, dividindo em partes menores, que podem ser
# chamadas de funções ou métodos.

# Exemplo de função:
# def nome_da_funcao(parametros):
#     codigo

def soma(a, b):
    print("A soma é igual a", a + b)

def subtracção (a, b):
    print("A subtração é igual a", a - b)

def multiplicação(a, b):
    print("A multiplicação é igual a", a * b)

def divisao(a, b):
    se b == 0:
        print("Não é possível dividir por zero")
    senão:
        print("A divisão é igual a", a / b)

# Chamada de função ou método  
numero = 10
numero2 = 20
soma(numero, numero2)

subtracção (numero, numero2)

multiplicação(numero, numero2)

divisao(numero, numero2)
 63 alterações: 63 adições e 0 exclusões63  
Aula08/Exercício.py
@@ -0,0 +1,63 @@
# Criar um menu para mostrar as funções disponíveis e o usuário selecionar qual
# função ele quer executar.

# Faça um Programa que peça dois números e imprima o maior deles.

def imprimir_maior_numero():
    número1 = input("Digite o primeiro número: ")

    número2 = input("Digite o segundo número: ")

    Experimente:
        numero1 = int(numero1)
        numero2 = int(numero2)
        se numero1 > numero2:
            print("O número", número1, "é maior que o número", número2)
        elif numero1 == numero2:
            print("Os números são iguais")
        senão:
            print("O número", número2, "é maior que o número", número1)
    exceto exceção:
        print("Você não digitou um número válido")
        sair()


def verificar_valor_positivo():
    # Faça um Programa que peça um valor e mostre na tela se o valor é positivo 
    # ou negativo.

    valor = int(input("Digite um valor: " ))

    se valor > 0:
        print("O valor é positivo")
    elif valor == 0:
        print("O valor é neutro")
    senão:
        print("O valor é negativo")

# Criar um menu para mostrar as funções disponíveis e o usuário selecionar qual
# função ele quer executar.
def menu():
    opção = 1  
    enquanto opcao != 0:
        print('----Seja bem vindo ao meu Super Menu----')
        print('Escolha uma opção abaixo:')
        print('1 - Imprimir maior número')
        print('2 - Verificar se o valor é positivo ou negativo')

        opcao = int(input('Digite uma das opções ou 0 para sair:'))
        se opcao == 1:
            print('---Iniciando a função imprimir_maior_numero---')
            imprimir_maior_numero()
            print('---Fim da função imprimir_maior_numero---')
        Elif Opcao == 2:
            print('---Iniciando a função verificar_valor_positivo---')
            verificar_valor_positivo()
            print('---Fim da função verificar_valor_positivo---')
        senão:
            print('Opção inválida')

        print('----Fim do menu ----')

# Chamar função de menu
menu()
