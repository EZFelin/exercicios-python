# Faça um programa que imprima os números múltiplos de 11 entre 1 e 200 usando um loop while.
x=1
while x<=200:
    x=x+1
    if x%11==0:
        print ("Esses são os numeros divisíveis por 11: ",x)
