# Faça um programa que leia o salário atual de um funcionário e a porcentagem de aumento. O programa deve calcular e mostrar o valor do aumento e o novo salário.
s=float(input("Me fale seu salário atual: "))
p=float(input("Me fale sua porcentagem de aumento: "))

x=(p*s)/100
m=(s+x)

print ("O seu valor de aumento é de: {:.2f}." .format (x))
print ("seu salário atual é de: {:.2f}." .format (m))
