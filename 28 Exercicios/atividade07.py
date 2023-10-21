#Faça um Programa que leia três números e mostre o maior e o menor deles.
n1=int(input("Digite o primeiro numero"))
n2=int(input("Digite o segundo numero"))
n3=int(input("Digite o terceiro numero"))

maior=n1
if n2 > n1 and n2 > n3:
    maior=n2
if n3 > n1 and n3 > n2:
    maior=n3
print(f"O maior numero digitado foi{maior}")












