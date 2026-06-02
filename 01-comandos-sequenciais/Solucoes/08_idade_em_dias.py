# Faça um programa que leia a idade de uma pessoa expressa em anos, meses e dias e mostre-a expressa apenas em dias.
anos=int(input("Escreva sua idade expressa em anos: "))
meses=int(input("Escreva sua idade expressa em meses: "))
dias=int(input("Escreva sua idade expressa em dias: "))
idade=(anos*365)+(meses*30)+ dias
print("Sua idade em dias é de: ",idade)
