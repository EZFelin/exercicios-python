# Escreva um programa que leia uma lista de 10 números e imprima as posições dos valores que são menores que a média dos números da lista. O programa deve calcular a média dos números inseridos e, em seguida, percorrer a lista para identificar quais valores são menores que a média, imprimindo as posições correspondentes. Se nenhum valor for menor que a média, o programa deve informar ao usuário que não há valores menores que a média.
vet = []
soma = 0
for i in range(10):
    n = int(input("Digite um número: "))
    vet.append(n)
    soma += n

media = soma / 10

print("Posições dos valores menores que a média:")

for i in range(10):
    if vet[i] < media:
        print(i)