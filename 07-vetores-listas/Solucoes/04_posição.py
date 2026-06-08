# Escreva um programa que leia uma lista de 10 números e imprima as posições onde um número específico aparece na lista. O programa deve solicitar ao usuário o número a ser pesquisado e, em seguida, percorrer a lista para encontrar todas as ocorrências do número, imprimindo as posições correspondentes. Se o número não for encontrado na lista, o programa deve informar ao usuário que o número não está presente.
def repetidos(vet,val):
    found = False
    for i in range(len(vet)):
        if vet[i]==val:
            print("Posição ",i)
            found = True
    if not found:
        print("Número não encontrado na lista.")
lista=[2,5,3,5,77,5,1,4,3,9]
print(lista)
repetidos(lista,3)
