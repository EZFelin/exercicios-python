# Escreva um programa que leia um número inteiro positivo e imprima o seu reverso. O programa deve continuar lendo números até que o usuário digite o número 0 (zero).
def reverso(numero):
    invertido = 0
    while numero > 0:
        digito = numero % 10
        invertido = invertido * 10 + digito
        numero = numero // 10
    return invertido

num = int(input("Digite um número (0 para sair): "))
while num != 0:
    print("Reverso:", reverso(num))
    num = int(input("Digite um número (0 para sair): "))