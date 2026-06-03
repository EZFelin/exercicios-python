# Faça um programa que solicite ao usuário dois números de 3 dígitos e verifique se eles possuem os mesmos dígitos, independentemente da ordem. Por exemplo, os números 123 e 321 possuem os mesmos dígitos, enquanto os números 123 e 456 não possuem os mesmos dígitos.
numero1=int(input("Escreva o primeiro número de 3 dígitos: "))
numero2=int(input("Escreva o segundo número de 3 dígitos: "))
a1=numero1//100
resto=numero1%100
a2=resto//10
a3=resto%10
b1=numero2//100
resto=numero2%100
b2=resto//10
b3=resto%10
if (a1==b1 and a2==b2 and a3==b3) or (a1==b1 and a2==b3 and a3==b2):
    print("tem os mesmos dígitos!")
elif (a1==b2 and a2==b1 and a3==b3) or (a1==b2 and a2==b3 and a3==b1):
    print("tem os mesmos dígitos!")
elif (a1==b3 and a2==b1 and a3==b2) or (a1==b3 and a2==b2 and a3==b1):
    print("tem os mesmos dígitos!")
else:
    print("não tem os mesmos dígitos.")
