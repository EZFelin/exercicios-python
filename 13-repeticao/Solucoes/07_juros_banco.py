# Escreva um programa que leia um valor inicial, e calcule o número de meses necessários para que esse valor atinja ou ultrapasse 1000 reais, considerando uma taxa de juros de 5% ao mês. O programa deve utilizar a estrutura de repetição while para calcular o valor acumulado a cada mês, e a estrutura de decisão if para verificar se o valor atingiu ou ultrapassou 1000 reais. O programa deve imprimir o número de meses necessários para atingir ou ultrapassar 1000 reais para o usuário.
v=float(input("Valor:"))
j=v*0.05
nv=v+j
nj=1
m=1
while nj<1000:
    j=nv*0.05
    nj=nj+j
    m=m+1
print(m)
