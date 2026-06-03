# Faça um programa que gere um número aleatório entre 1 e 10 e solicite ao usuário que tente adivinhar o número. O programa deve continuar solicitando palpites até que o usuário acerte o número, e ao final deve informar quantas tentativas foram necessárias para acertar.
import random
h=(random.randint(1, 10))
z=0
c=0
while z!=h :
    z=int(input("Tente adivinhar o número entre 1 a 10: "))
    c=c+1
print("Você acertou! com o total de: ",c," tentativas")
