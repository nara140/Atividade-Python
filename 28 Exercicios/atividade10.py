#Faça um Programa que pergunte em que turno você estuda.
#Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
#Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.


turno = input("Em que turno você estuda? para M-Matutino, V-Vespertino e N-Noturno: ")


if turno == "M" or turno == "m":
    print("Bom Dia!")

elif turno == "V" or turno == "v":
    print("Boa Tarde!")

elif turno == "N" or turno == "n":
    print("Boa Noite!")

else:
    print("Valor Inválido!")


exit()
    