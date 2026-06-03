# Faça um programa que imprima os primeiros 100 números da série de Fibonacci usando um loop while. A série de Fibonacci é definida como: F(0) = 0, F(1) = 1, e F(n) = F(n-1) + F(n-2) para n > 1.
a = 0
b = 1
cont = 0
while cont < 100:
    print(a)
    prox = a + b
    a = b
    b = prox
    cont += 1