# Escreva um programa que leia uma sequência de números inteiros, e determine se a sequência é crescente, decrescente ou aleatória. O programa deve permitir que o usuário insira a quantidade de números que deseja digitar, e em seguida, os números da sequência. O programa deve utilizar a estrutura de repetição for para ler os números da sequência, e a estrutura de decisão if-elif-else para determinar o tipo da sequência. O programa deve imprimir o resultado para o usuário.
# - estritamente crescente (cada número digitado sempre é maior que o anterior)
# - crescente (cada número digitado é maior ou igual ao anterior)
# - estritamente decrescente (cada número digitado sempre é menor que o anterior)
# - decrescente (cada número digitado é menor ou igual ao anterior)
# - aleatória (a sequência não é crescente nem decrescente)
n=int(input("ESCREVA A QUANTIDADE DE NUMEROS QUE DEVE DIGITAR: "))
cresc=0
decresc=0
igual=0
cont=0
contm=0
conth=0
contt=0

n1=int(input("Número: "))
for i in range(n-1):
    n2=int(input("Nmr: "))
    if n1<n2:
        cont=cont+1
    if n1>n2:
        contm=contm+1
    if n1>=n2:
        conth=conth+1
    if n1<=n2:
        contt=contt+1
    n1=n2
        
    x=x+1 
    if contm>n-1:
        b='Estritamente crescente'
    elif conth>=n-1:
        b='Crescente'
    elif cont>n-1:
        b='Estritamente decrescente'
    elif contt<=n-1:
        b='Decrescente'
    else:
        b='Aleatória'
print(b)
    
    
