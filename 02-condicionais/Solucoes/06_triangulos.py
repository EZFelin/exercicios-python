# Faça um programa que solicite ao usuário os valores dos lados de um triângulo e determine se eles formam um triângulo válido. Se forem válidos, classifique o tipo de triângulo (equilátero, isósceles ou escaleno).
a=float(input("Valor de a: "))
b=float(input("Valor de b: "))
c=float(input("Valor de c: "))
if a+b>c or a+c>b or b+c>a :
    if a==b==c :
        if a!=b or a!=c or c!=b :
            print("Esse é um triângulo isósceles")
        else:
            print("Esse é um triângulo equilatero")
    else:
        print("Esse é um triângulo escaleno")
else:
    print("NÃO É TRIANGULO")
