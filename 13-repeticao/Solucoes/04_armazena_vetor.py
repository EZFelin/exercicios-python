# Escreva um programa que leia 10 números inteiros, armazene-os em um vetor, e imprima os índices dos números que são menores do que a média dos números digitados. O programa deve utilizar a estrutura de repetição for para ler os números e calcular a média, e a estrutura de decisão if para comparar cada número com a média. O programa deve imprimir os índices dos números menores do que a média para o usuário.
v=[]
soma=0
for i in range (10):
    x=int(input("Escreva dez números inteiros: "))
    v.append(x)
    soma=soma+x
med=soma/i
for i in range (10):
    if v[i]<med:
        print(" ",i)
