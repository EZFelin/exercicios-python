# Escreva um programa que leia 5 números inteiros e imprima quantos estão entre 10 e 20 (inclusive), quantos são menores que 10 e quantos são maiores que 20.
q=5
entre=0
cont10=0
cont20=0
for cont in range(q):
    n=int(input('numero:'))
    if n>=10 and n<=20:
        entre=entre+1
    elif n<10:
        cont10=cont10+1
    else:
        cont20=cont20+1
print("Esta é a quantidade de numeros que estão entre 10 e 20: ",entre)
print("Esta é a quantidade de numeros abaixo de 10: ",cont10)
print("Esta é a quantidade de numeros acima de 20: ",cont20)
