# Escreva um programa que leia uma lista de 7 números e ordene a lista em ordem crescente usando o algoritmo de ordenação Bubble Sort. Em seguida, imprima a lista ordenada. Além disso, modifique o programa para permitir que o usuário escolha se deseja ordenar a lista em ordem crescente ou decrescente. 
def bubblesort(v):
    n=len(v)
    for i in range (n-1):
        for j in range (0, n-i-1):
            if v[j]<v[j+1]:
                aux=v[j]
                v[j]=v[j+1]
                v[j+1]=aux




vet=[]
for i in range (7):
    n=float(input("Escreva: "))
    vet.append(n)
print("Lista=",vet)


bubblesort(vet)
print("Lista ordenada= ",vet)




# MAIS BONITO
def bubblesort(v,tipo):
    n=len(v)
    for i in range (n-1):
        for j in range (0, n-i-1):
            if tipo==0:
                if v[j]>v[j+1]:
                    aux=v[j]
                    v[j]=v[j+1]
                    v[j+1]=aux
            else:
                 if v[j]<v[j+1]:
                        aux=v[j]
                        v[j]=v[j+1]
                        v[j+1]=aux




vet=[]
for i in range (7):
    n=float(input("Escreva: "))
    vet.append(n)
print("Lista=",vet)


bubblesort(vet,0)
print("Lista ordenada crescente= ",vet)
bubblesort(vet,1)
print("Lista ordenada decrescente= ",vet)
