# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3%
# e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que 
# calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população
# do país B, mantidas as taxas de crescimento.

paisA = 80000
paisB = 200000
crecimentoPaisA = 3/100
crecimentoPaisB = 1.5/100
ano = 0
while paisA <= paisB:
    paisA += (paisA * crecimentoPaisA)
    paisB += (paisB * crecimentoPaisB)
    ano += 1
    print(f"Ano {ano:>2} Pais A{paisA : >5.0f} e pais B{paisB :>5.0f}")
    print("levara",ano,"anos para populacao da cidade A ficar maior que da cidade B")