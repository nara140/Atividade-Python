# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
# sabendo que a decisão é sempre pelo mais barato.

 
p1=input("digite o primeiro valor")
p2=input("digite o segundo valor")
p3=input("digite o terceiro valor")

menor=p1
if p2 < p1 and p2 < p3:
    menor=p2
if p3 < p1 and p3 < p2:
    menor=p3

print(f"compre o {menor}.")

