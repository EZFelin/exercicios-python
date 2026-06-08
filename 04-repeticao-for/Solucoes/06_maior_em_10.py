# Escreva um programa que leia 10 números inteiros positivos e imprima o maior número da sequência.
q=10
maior=0
for cont in range(q):
    n=int(input('numero:'))
    while n<=0:
        n=int(input("Numero inválido! número= "))
    if n>maior:
        maior=n
print("O maior número é: ",maior)
