#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.
numero=int(input("digite um numero"))
primo= True
for n in range(2,numero):
    if numero % n==0:
        print("nao e primo",n,"e divisor")
        primo = False
    if primo:
        print("e primo")
        