# Escreva um programa que leia dois vetores de 7 números cada, crie um terceiro vetor que seja a junção dos dois vetores anteriores e ordene o terceiro vetor em ordem crescente. Em seguida, imprima o vetor ordenado.
vx=[]
vy=[]
vz=[]
for i in range(0,7):
    n=int(input("Digite um número(vetor x): "))
    vx.append(n)
for i in range(0,7):
    n=int(input("Digite um número(vetor y): "))
    vy.append(n)
for i in range(0,7):
    vz.append(vx[i])
    vz.append(vy[i])
for x in range(0,14):
    for i in range(0,14):
        if vz[x]<vz[i]:
            aux=vz[x]
            vz[x]=vz[i]
            vz[i]=aux
print("Vetor z: ")
for i in range(0,14):
    print(vz[i]," ")
