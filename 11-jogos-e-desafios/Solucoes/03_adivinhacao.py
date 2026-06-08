# Escreva um programa que simule um jogo de adivinhação, onde o computador escolhe aleatoriamente um número entre 1 e 10, e o usuário tem que adivinhar qual é esse número. O programa deve permitir que o usuário faça várias tentativas até que ele acerte o número, e deve contar quantas tentativas foram necessárias para adivinhar o número. Ao final do jogo, o programa deve imprimir a quantidade de tentativas necessárias para adivinhar o número, e perguntar se o usuário deseja jogar novamente.
import random
x=(random.randint(1,10))
n=1
quant=0
while n:
    quant=quant+1
    n=int(input("Digite um número entre 1 a 10: "))
    if n<1 and n>10:
        n=int(input("Número Inválido! Digite um número entre 1 a 10: "))
    if n==x:
        print("Essa foi a quantidade de tentativas necessárias para adivinhar o número: ",quant)
        y=str(input("Você acertou!!! Se deseja continuar aperte s se não aperte n: "))
        if y=='s':
            x=(random.randint(1,10))
            n=1
        if y=='n':
            print('Muito obrigado por jogar!')
