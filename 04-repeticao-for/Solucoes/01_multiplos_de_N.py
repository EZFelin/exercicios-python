# Escreva um programa que leia um número inteiro N (entre 2 e 19) e imprima os 300 primeiros múltiplos de N.
quant=0
n=int(input("Escreva um numero entre 2 e 19: "))
for cont in range(1,301):
    quant=quant+1
    if quant%n==0:
        print(quant)
