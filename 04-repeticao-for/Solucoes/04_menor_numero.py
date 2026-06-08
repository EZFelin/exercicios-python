# Escreva um programa que leia uma sequência de números inteiros positivos e imprima o menor número da sequência. A sequência termina quando o usuário digitar o número 0 (zero).
menor=999999
n=1
while n!=0:
    n=int(input("Digite um número: "))
    if n>0:
      if n<menor:
          menor=n
print("Esse é o menor número: ",menor)
