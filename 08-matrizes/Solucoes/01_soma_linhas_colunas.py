# Escreva um programa que leia uma matriz de 5 linhas e 3 colunas, preenchida pelo usuário, e calcule a soma dos elementos de cada linha e de cada coluna. O programa deve armazenar as somas das linhas em um vetor separado e as somas das colunas em outro vetor separado. Por fim, o programa deve imprimir a matriz original, as somas das linhas e as somas das colunas.
mat=[]
vet=[]
somalinhas=[]
somacolunas=[]
for l in range (5):
    for c in range(3):
        n=int(input("Escreva números: ["+str(l)+"]["+str(c)+"]"))
        vet.append(n)
    mat.append(vet)
    vet=[]
    
somalin=0
for l in range (5):
    for c in range(3):
        somalin=somalin+mat[l][c]
    somalinhas.append(somalin)
    somalin=0
    
somacol=0
for c in range (3):
    for l in range(5):
        somacol=somacol+mat[l][c]
    somacolunas.append(somacol)
    somacol=0


print("Essa é a matriz: ",mat)
print("Essa é a matriz: ",somalinhas)
print("Essa é a matriz: ",somacolunas)
