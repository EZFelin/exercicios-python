# Escreva um programa que leia uma lista de 10 números e permita ao usuário verificar quantas vezes um número específico aparece na lista. O programa deve solicitar ao usuário o número a ser verificado e, em seguida, percorrer a lista para contar quantas vezes o número aparece, imprimindo o resultado final. Se o número não for encontrado na lista, o programa deve informar ao usuário que o número não está presente.
lista = []
for i in range(0,10):
    n=int(input("Escreva números inteiros: "))
    lista.append(n)
num=int(input("Escreva um número para ver quantas vezes aparece: "))
cont=0
for i in range(0,10):
    if lista[i]==num:
        cont=cont+1
if cont==0:
    print("Número não encontrado na lista.")
else:
    print("Essa é a quantidade de vezes que ele aparece repetido na lista: ",cont)


