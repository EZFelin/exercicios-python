# Escreva um programa que leia uma lista de 10 números e imprima a quantidade de valores diferentes presentes na lista, bem como os próprios valores diferentes. O programa deve solicitar ao usuário que insira os 10 números, armazená-los em uma lista e, em seguida, percorrer a lista para identificar os valores únicos. O programa deve contar quantos valores diferentes existem na lista e imprimir essa quantidade, juntamente com os valores únicos encontrados. Se todos os números forem iguais, o programa deve informar ao usuário que há apenas um valor diferente.
vet = []
for i in range(10):
    n = int(input("Digite um valor: "))
    vet.append(n)

diferentes = []

for i in range(10):
    if vet[i] not in diferentes:
        diferentes.append(vet[i])

print("Quantidade de valores diferentes:", len(diferentes))
print("Valores diferentes:", diferentes)