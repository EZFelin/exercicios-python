# Escreva um programa que leia a hora de início e a hora de fim de um período, e imprima as consultas geradas a cada 15 minutos dentro desse período. O programa deve utilizar a estrutura de repetição for para gerar as consultas, e a estrutura de decisão if para verificar se as horas digitadas são válidas. O programa deve imprimir as consultas geradas para o usuário, e o total de consultas geradas no final.
hff=0
i=0
hi=int(input("Escreva a hora de início: "))
hf=int(input("Escreva a hora de fim: "))
if (hi>24 and hi<1 or hf>24 and hf<1):
    print("Horas erradas")
    hi=int(input("Escreva a hora de início: "))
    hf=int(input("Escreva a hora de fim: "))
hii=hi
for i in range(((hf-hi)*4)+1):
    i=i+1
    print(hii,":",hff)
    hff=hff+15
    if(hff==60):
        hii=hii+1
        hff=00
print(i,"Consultas Geradas")
