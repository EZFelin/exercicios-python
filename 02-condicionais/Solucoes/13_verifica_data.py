# Faça um programa que solicite ao usuário uma data (dia, mês e ano) e verifique se a data é válida. Considere os seguintes critérios para validar a data:
# - O dia deve ser um número entre 1 e 31, dependendo do mês.
dia=int(input("Digite um dia: "))
mes=int(input("Digite um mês(em números): "))
ano=int(input("Digite um ano: "))
if mes==4 or mes==6 or mes==9 or mes==11 and dia>=1 and dia<=30:
    print("A data ",dia,"/",mes,"/",ano," é válida.")
if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12 and dia>=1 and dia<=31:
    print("A data ",dia,"/",mes,"/",ano," é válida.")
if mes==2 and dia>=1 and dia<=28:
    print("A data ",dia,"/",mes,"/",ano," é válida.")
else:
    print("A data está incorreta.")
