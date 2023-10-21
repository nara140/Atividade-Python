#Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
#Dica: utilize o operador módulo (resto da divisão).
def impar_ou_par():

    numero = int(input("Digite um número inteiro: "))

    if numero % 2 == 0:
        print("numero é um número par.")
    else:
        print("numero é um número ímpar.")

#Faça um Programa que leia um número inteiro menor que 1000
# e imprima a quantidade de centenas, dezenas e unidades do mesmo.
#Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
#326 = 3 centenas, 2 dezenas e 6 unidades
#12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10,

def media():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))


    media = (nota1 + nota2 + nota3) / 3

    if media == 10:
        situacao = "Aprovado com Distinção"
    elif media >= 7:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    print("Situação do aluno:",situacao)
    print("Média alcançada:", media)
    
    # Criar um menu para mostrar as funções disponíveis e o usuário selecionar qual
# função ele quer executar.
def menu():
    print('Seja bem vindo ao Menu')
    print('Escolha uma opção abaixo:')
    print('1 - verificar se o numero e impar ou par')
    print('2 - Verificar media')

    opcao = int(input('Digite uma das opções ou 0 para sair:'))
    if opcao==1:
        print("verificando se e impar ou par")
        impar_ou_par()
        print("fim da verificaçao impar ou par")
    elif opcao == 2:
        print("iniciando calculo de media")
        media()
    if opcao == 0:
        print("fim do menu")





