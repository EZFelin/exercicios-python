# Escreva um programa que leia uma lista de 10 números e imprima os números pares e ímpares separadamente. O programa deve percorrer a lista e identificar quais números são pares e quais são ímpares, armazenando-os em listas separadas. Em seguida, o programa deve imprimir as listas de números pares e ímpares.
lista = []
for i in range(0,10):
    n=int(input("Escreva números inteiros: "))
    lista.append(n)
print("Esses são pares: ")
for i in range(0,10):
    if lista[i]%2==0:
        print(lista[i], " ")
print("Esses são ímpares: ")
for i in range (0,10):
    if lista[i]%2!=0:
        print(lista[i], " ")
