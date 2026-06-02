# Faça um programa que leia a data de nascimento de uma pessoa (dia, mês e ano) e uma data posterior a essa data (dia, mês e ano). O programa deve calcular quantos anos, meses e dias se passaram entre as duas datas. Considere que um ano tem 365 dias e um mês tem 30 dias.
dia=int(input("Escreva o dia de nascimento de uma pessoa,dia: "))
mes=int(input("Escreva o mês de nascimento de uma pessoa,mês: "))
ano=int(input("Escreva o ano de nascimento de uma pessoa,ano: "))
diapost=int(input("Escreva um dia posterior a essa data: "))
mespost=int(input("Escreva um mês posterior a essa data: "))
anopost=int(input("Escreva um ano posterior a essa data: "))
diasnasceu=dia+(mes*30)+(ano*365)
print(f"Você nasceu há {diasnasceu} dias")
diasposterior=diapost+(mespost*30)+(anopost*365)
print(f"A data do cálculo foi há {diasposterior} dias")
total=diasposterior-diasnasceu
anos=total//365
resto=total%365
meses=resto//30
dias=resto%30
print("Do seu nascimento até a data passaram-se")
print(f"{anos} anos, {meses} meses e {dias} dias")
