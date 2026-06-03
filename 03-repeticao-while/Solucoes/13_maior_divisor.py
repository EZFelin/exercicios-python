# Faça um programa que solicite ao usuário um número inteiro maior que 1 e imprima o maior divisor inteiro desse número (exceto ele mesmo) usando um loop while.
n = int(input("Digite um número inteiro maior que 1: "))
div = n - 1
while div > 0:
    if n % div == 0:
        print("Maior divisor:", div)
        break
    div -= 1