# Escreva um programa que leia um número inteiro N e imprima todos os divisores inteiros de N.
quant=0
n=int(input("Escreva um numero: "))
for cont in range(1,n+1):
    quant=quant+1
    y=n%quant
    if y==0:
        print(quant)
