# Escreva um programa que leia uma lista de 10 números e permita ao usuário inserir um novo número em uma posição específica da lista. O programa deve solicitar ao usuário o número a ser inserido e a posição onde ele deve ser inserido. Em seguida, o programa deve atualizar a lista com o novo número na posição especificada e imprimir a lista atualizada. Se a posição especificada for inválida (menor que 0 ou maior que o tamanho da lista), o programa deve exibir uma mensagem de erro e não realizar a inserção.
def insere(vet,pos,val):
    if pos<0 or pos>len(vet):
        print("ERRO!!!!!")
        return
    vet.append(val)
    i=len(vet)-1
    while i>pos:
            aux=vet[i]
            vet[i]=vet[i-1]
            vet[i-1]=aux
            i=i-1
            
lista=[2,5,12,3,78]
print(lista)
insere(lista,2,55)
print(lista)
insere(lista,0,10)
print(lista)
