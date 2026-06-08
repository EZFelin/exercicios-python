# Escreva um programa que leia o peso e a altura de 10 pessoas, armazenando esses valores em listas separadas. O programa deve calcular a média das alturas e, em seguida, imprimir o peso e a altura das pessoas que têm altura acima da média. Se nenhuma pessoa tiver altura acima da média, o programa deve informar ao usuário que não há pessoas com altura acima da média.
pesos = []
alturas = []
soma_alturas = 0

for i in range(10):
    peso = float(input("Peso: "))
    altura = float(input("Altura: "))

    pesos.append(peso)
    alturas.append(altura)

    soma_alturas += altura

media = soma_alturas / 10

print("Pessoas com altura acima da média:")

for i in range(10):
    if alturas[i] > media:
        print("Peso:", pesos[i], "Altura:", alturas[i])