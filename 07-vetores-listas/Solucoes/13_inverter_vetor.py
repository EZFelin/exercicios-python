# Escreva um programa que leia um vetor de 10 números e imprima o vetor invertido. O programa deve solicitar ao usuário que insira os 10 números, armazená-los em um vetor e, em seguida, percorrer o vetor de trás para frente para imprimir os números na ordem inversa. O programa deve garantir que o vetor seja preenchido corretamente antes de tentar imprimir os valores invertidos.
vet = []
tam = int(input("Tamanho do vetor: "))
for i in range(tam):
    n = int(input("Digite um valor: "))
    vet.append(n)

inicio = 0
fim = tam - 1

while inicio < fim:
    aux = vet[inicio]
    vet[inicio] = vet[fim]
    vet[fim] = aux

    inicio += 1
    fim -= 1

print(vet)