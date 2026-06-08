# Escreva um programa que leia a quantidade de participantes online em um evento durante um período de tempo. O programa deve armazenar as quantidades em uma lista e, ao final, apresentar as menores e maiores quantidades de participantes online. O programa deve continuar lendo as quantidades até que o usuário digite 0 para indicar o fim da entrada de dados.
participantes = []
numero = int(input("Digite a quantidade de participantes (0 para parar): "))

while numero != 0:
    participantes.append(numero)
    numero = int(input("Digite a quantidade de participantes (0 para parar): "))

participantes.sort()

print("Menores participações:")
print(participantes[0], "e", participantes[1])

print("Maiores participações:")
print(participantes[-2], "e", participantes[-1])