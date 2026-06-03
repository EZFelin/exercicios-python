# Faça um programa que solicite ao usuário um ano e verifique se o ano é bissexto ou não. Considere os seguintes critérios para determinar se um ano é bissexto:
a=int(input("Escreva um ano: "))
if (a%4)==0 or (a%400)==0:
    print("O ano é bissexto")
elif (a%4)!=0 and (a%100)!=0:
    print("O ano não é bissexto")
