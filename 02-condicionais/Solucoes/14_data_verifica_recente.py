# Faça um programa que solicite ao usuário a data de nascimento de uma pessoa (dia, mês e ano) e a data atual (dia, mês e ano). Calcule a quantidade aproximada de dias que a pessoa viveu até a data atual. Considere os seguintes critérios para validar as datas:
# - O dia deve ser um número entre 1 e 31, dependendo do mês.
dia=int(input("Digite o dia de nascimento de uma pessoa: "))
mes=int(input("Digite o mes de nascimento de uma pessoa: "))
ano=int(input("Digite o ano de nascimento de uma pessoa: "))
diaa=int(input("Digite o dia atual: "))
mesa=int(input("Digite o mes atual: "))
anoa=int(input("Digite o ano atual: "))
qtd=(diaa+(mesa*30)+(anoa*365))-(dia+(30*mes)+(ano*365))
if mes==4 or mes==6 or mes==9 or mes==11 and dia>=1 and dia<=30:
    print("Válido")
elif mes==2 and dia>=1 and dia<=28:
    print("Válido")
if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12 and dia>=1 and  dia<=31:
    print("Válido")
else:
    print("Valor inválido")
if mesa==4 or mesa==6 or mesa==9 or mesa==11 and diaa>=1 and diaa<=30:
    print("Válido")
elif mesa==2 and diaa>=1 and diaa<=28:
    print("Válido")
if mesa==1 or mesa==3 or mesa==5 or mesa==7 or mesa==8 or mesa==10 or mesa==12 and diaa>=1 and  diaa<=31:
    print("Válido")
else:
    print("Valor inválido")
if anoa>ano:
    print("O valor aproximadamente que a pessoa viveu é de: ",qtd)
else:
    print("a data atual deve ser mais recente que a data de nascimento.")
