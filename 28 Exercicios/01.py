#Faça um Programa que peça dois números e imprima o maior deles.
numero=int(input("Digite o primeiro numero"))
numero2=int(input("digite o segundo numero"))
if numero > numero2: 
    maior=numero
if numero2 > numero:
    maior=numero2
print(f"O maior numero digitado foi{maior}")
