# Escreva um programa que leia uma data (dia, mês e ano) e verifique se a data é válida. Considere que fevereiro tem 29 dias em anos bissextos e 28 dias em anos não bissextos. O programa deve imprimir a data por extenso, caso seja válida, ou uma mensagem de erro caso contrário.
def bissexto(a):
    if a%4==0 and not(a%100==0):
        return True
    return False
    
def data(d,m,a):
    m31=(1,3,5,7,8,10,120)
    m30=(4,6,9,11)
    if d>=1 and m>=1:
        if d<=31 and m in m31:
             return True
        if m==2:
            if bissexto(a) and d<=29:
                return True
            if d<=28:
                return True
        if d<=30 and m in m30:
            return True
    return False
def escrevedata(d,m,a):
    texto=str(d)+" de "
    if m==1:
        ms="Janeiro"
    elif m==2:
        ms="Fevereiro"
    elif m==3:
        ms="Março"
    elif m==4:
        ms="abril"
    elif m==5:
        ms="Maio"
    elif m==6:
        ms="Junho"
    elif m==7:
        ms="Julho"
    elif m==8:
        ms="Agosto"
    elif m==9:
        ms="Setembro"
    elif m==10:
        ms="Outubro"
    elif m==11:
        ms="Novembro"
    elif m==12:
        ms="Dezembro"
    texto=texto+ms+" de "+str(a)
    return texto
        

dia=int(input("Digite um dia: "))
mes=int(input("Digite um mês(em números): "))
ano=int(input("Digite um ano: "))
if data(dia,mes,ano):
    print(escrevedata(dia,mes,ano))
else:
    print("Data Inválida")
