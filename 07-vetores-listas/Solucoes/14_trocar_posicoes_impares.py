# Escreva um programa que leia um vetor de 10 números e troque as posições dos números ímpares com os números pares. O programa deve solicitar ao usuário que insira os 10 números, armazená-los em um vetor e, em seguida, percorrer o vetor para identificar quais números são pares e quais são ímpares. O programa deve trocar as posições dos números ímpares com os números pares, garantindo que os números pares fiquem nas posições ímpares do vetor e os números ímpares fiquem nas posições pares do vetor. Por fim, o programa deve imprimir o vetor resultante após a troca de posições.
vet = []
for i in range(10):
    n = int(input("Digite um valor: "))
    vet.append(n)

for i in range(0, 9, 2):
    aux = vet[i]
    vet[i] = vet[i + 1]
    vet[i + 1] = aux

print(vet)