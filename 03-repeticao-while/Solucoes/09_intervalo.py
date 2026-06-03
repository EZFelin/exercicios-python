# Faça um programa que solicite ao usuário que digite 15 números inteiros e, em seguida, imprima quantos desses números estão entre 10 e 20 (inclusive).
x=1
cont=0
while x<=15:
    n=int(input("Digite números: "))
    x=x+1
    if n>=10 and n<=20:
        cont=cont+1
print ("Há",cont,"números entre 10 e 20")
