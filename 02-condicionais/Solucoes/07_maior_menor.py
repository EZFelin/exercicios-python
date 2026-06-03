# Faça um programa que solicite ao usuário três números e determine qual é o maior e qual é o menor entre eles. O programa deve considerar a possibilidade de os números serem iguais e informar adequadamente.
a=float(input("Valor de n1: "))
b=float(input("Valor de n2: "))
c=float(input("Valor de n3: "))
if a>b and a>c:
    print("O número maior é:",a)
if b>a and b>c:
    print("O número maior é:",b)
if c>b and c>a:
    print("O número maior é:",c)
if a<b and a<c:
    print("O número menor é:",a)
if b<a and b<c:
    print("O número menor é:",b)
if c<b and c<a:
    print("O número menor é:",c)
if a==b==c:
    print("São iguais")
if a!=b and b!=c and c!=a:
    print("São todos diferentes")
