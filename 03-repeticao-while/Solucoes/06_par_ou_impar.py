# Faça um programa que solicite ao usuário um número inteiro N e, em seguida, solicite que o usuário digite N números inteiros. Para cada número digitado, o programa deve informar se ele é par ou ímpar.
n = int(input("Digite um numero inteiro que quer digitar: "))
x = 1
while x<=n:
    y = int(input("Digite um numero inteiro: "))
    x=x+1
    if (y%2==0):
        print("par")
    else:
        print("impar")
