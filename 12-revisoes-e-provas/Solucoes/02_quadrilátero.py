# Escreva um programa que leia os valores dos quatro lados de um quadrilátero, e determine se ele é um quadrado, um retângulo, um trapézio ou um quadrilátero comum. O programa deve imprimir o resultado para o usuário. O programa deve utilizar a estrutura de decisão if-elif-else para realizar a verificação.
n1=float(input("Escreva o valor do lado 1: "))
n2=float(input("Escreva o valor do lado 2: "))
n3=float(input("Escreva o valor do lado 3: "))
n4=float(input("Escreva o valor do lado 4: "))
if n1>n2:
    aux=n1
    n1=n2
    n2=aux
if n1>n3:
    aux=n1
    n1=n3
    n3=aux
if n1>n4:
    aux=n1
    n1=n4
    n4=aux
if n2>n1:
    aux=n2
    n2=n1
    n1=aux
if n2>n3:
    aux=n2
    n2=n3
    n3=aux
if n2>n4:
    aux=n2
    n2=n4
    n4=aux
if n3>n1:
    aux=n3
    n3=n1
    n1=aux
if n3>n2:
    aux=n3
    n3=n2
    n2=aux
if n3>n4:
    aux=n3
    n3=n4
    n4=aux
if n4>n1:
    aux=n4
    n4=n1
    n1=aux
if n4>n2:
    aux=n4
    n4=n2
    n2=aux
if n4>n1:
    aux=n4
    n4=n3
    n3=aux
print("A Ordem decrescente é: ",n4,n3,n2,n1)
if n1==n2==n3==n4:
    print("Quadrado")
elif (n1==n2 and n3==n4) or (n1==n3 and n2==n4) or (n3==n1 and n4==n1):
    print("Retângulo")
elif (n1==n2 and n3!=n4) or (n1==n3 and n2!=n4) or (n3==n1 and n4!=n1) or (n3==n4 and n1!=n2) or (n2==n4 and n1!=n3) or (n4==n1 and n3==n1):
    print("Trapézio")
else:
    print("Quadrilátero")
