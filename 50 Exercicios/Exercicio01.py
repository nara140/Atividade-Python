#faça um programa que peça uma nota,entre zero e dez.Mostre uma mensagem caso o valor seja inválido e continue pedindo ate que o
nota=float(input("digite sua nota:"))
while 0 > nota or 10 < nota:
    nota=float(input())


