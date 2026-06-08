# Escreva um programa que leia um número inteiro N e imprima o maior divisor inteiro de N, além de imprimir a quantidade de divisores inteiros de N.
quant=0
maior=0
n=int(input("Digite um numero acima de 1: "))
if n<=1:
    n=int(input("Valor Inválido! Digite um número acima de 1: "))
while quant<n:
    quant=quant+1
    y=n%quant
    if y==0:
        print(quant)
    if quant>maior:
        maior=quant
print("Esse é o maior valor: ",maior)
