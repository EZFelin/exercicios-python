# Escreva um programa que leia o peso e a altura de 10 pessoas, armazene-os em vetores, e imprima o peso e a altura das pessoas que têm altura maior do que a média das alturas digitadas. O programa deve utilizar a estrutura de repetição for para ler os pesos e as alturas, calcular a média das alturas, e comparar cada altura com a média. O programa deve imprimir o peso e a altura das pessoas com altura maior do que a média para o usuário.
v=[]
vet=[]
soma=0
for i in range(10):
    print("Pessoa ",i+1,":")
    p=float(input("Escreva o seu peso: "))
    v.append(p)
    a=float(input("Escreva a sua altura: "))
    vet.append(a)
    soma=soma+a
med=soma/10
for i in range(10):
    if vet[i]>med:
        print("Pessoa ",i+1,": peso ",v[i],"kg e altura ",vet[i])