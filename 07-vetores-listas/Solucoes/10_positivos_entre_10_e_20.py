# Escreva um programa que leia uma lista de 10 números e imprima apenas os números positivos que estão entre 10 e 20 (inclusive) em ordem inversa. O programa deve percorrer a lista, identificar os números que atendem aos critérios e armazená-los em uma nova lista. Em seguida, o programa deve imprimir os números positivos entre 10 e 20 em ordem inversa.
numeros = []
while len(numeros) < 10:
    n = int(input("Digite um número: "))

    if n > 0 and n >= 10 and n <= 20:
        numeros.append(n)

print("Ordem inversa:")

for i in range(len(numeros)-1, -1, -1):
    print(numeros[i])