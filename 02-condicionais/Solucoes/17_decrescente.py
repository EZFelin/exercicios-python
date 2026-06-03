# Faça um programa que solicite ao usuário três números inteiros e os imprima em ordem decrescente. Considere os seguintes critérios para validar os números:
# - Os números devem ser inteiros.
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
if a>b:
    aux=a
    a=b
    b=aux
if b>c:
    aux=b
    b=c
    c=aux
if a>b:
    aux=a
    a=b
    b=aux
print("Ordem Deecrescente:",c,b,a)
