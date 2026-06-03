# Faça um programa que solicite ao usuário que digite números inteiros positivos até que ele digite 0. O programa deve imprimir o menor número positivo informado pelo usuário. Se nenhum número positivo for informado, o programa deve exibir uma mensagem indicando isso.
menor = True
while True:
    nmr = int(input("Digite um número (0 para encerrar): "))
    if nmr == 0:
        break
    if nmr > 0:
        if menor is True or nmr < menor:
            menor = nmr
if menor is not True:
    print("Menor número positivo informado:", menor)
else:
    print("Nenhum número positivo foi informado.")