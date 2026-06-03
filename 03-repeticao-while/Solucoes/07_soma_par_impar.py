# Faça um programa que solicite ao usuário um número inteiro N e, em seguida, solicite que o usuário digite N números inteiros. Para cada número digitado, o programa deve informar se ele é par ou ímpar. Ao final, o programa deve imprimir a soma dos números pares e a soma dos números ímpares digitados pelo usuário.
n = int(input("Digite um numero inteiro que quer digitar: "))
x = 1
soma=0
somai=0
while x<=n:
    y = int(input("Digite um numero inteiro: "))
    x=x+1
    if (y%2==0):
        print("par")
        soma=soma+y
    else:
        print("impar")
        somai=somai+y
print("A soma dos numeros pares é de: ",soma)
print("A soma dos numeros impares é de: ",somai)
