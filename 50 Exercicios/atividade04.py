# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

nome=input("Digite seu nome")
while len(nome) < 3:
    print("Quantidade de caracteres no nome esta menor que 3 carcteres")
if len(nome) < 3:
    nome = input("Digite seu nome:")

idade=int(input("Digite sua idade"))
while idade < 0 or idade > 150:
    print("Idade invalida")
    if idade < 0 or idade > 150:
        idade = int(input("digite sua idade"))

salario= float(input("Digite seu salario"))
while salario <= 0:
    print("salario invalido") 
    if salario <= 0:
        salario = float(input("Digite seu salario"))  

sexo= input("Digite o sexo(f ou m):")
while sexo != "f" and sexo !="m":
    print("Sexo invalido")
    if sexo != f and sexo != "m":
        sexo= input("Digite o sexo(f ou m):")

EstadoCivil= input("Digite o estado civil(s,c,v,d):")
while EstadoCivil !="s" and EstadoCivil != "c" and EstadoCivil != "v" and EstadoCivil != "d":
    print("Estado Civil invalido")
    if EstadoCivil != "s" and EstadoCivil != "c" and EstadoCivil != "v" and EstadoCivil != "d":
        EstadoCivil = input("Digite o estado civil (s,c,v,d):") 
               
