# Faça um programa que solicite ao usuário um número inteiro positivo N e imprima todos os divisores inteiros de N usando um loop while.
n=int(input("Digite um número inteiro positivo: "))
x=1
while x<=n:
    if n%x==0:
        print(x)
    x=x+1
