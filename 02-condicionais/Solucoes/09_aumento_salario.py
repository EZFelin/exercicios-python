# Faça um programa que solicite ao usuário o valor do salário de um funcionário e calcule o novo salário com base nas seguintes regras de aumento:
# - Se o salário for superior a R$ 1250,00, o aumento será de 6%.
# - Se o salário for igual ou inferior a R$ 1250,00, o aumento será de 8%. 
a=float(input("Valor do salário: "))
b=1250
if a>b:
    print("Esse é seu aumento caso ganhe um salário superior á $1250: ",a+(a*6)/100)
if a<=b:
    print("Esse é seu aumento caso ganhe um salário inferior ou igual á $1250: ",a+(a*8)/100)
