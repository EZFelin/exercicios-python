# Escreva um programa que leia uma matriz 3x3 de números inteiros, e determine quais são os números perfeitos presentes na matriz. Um número perfeito é um número inteiro positivo que é igual à soma de seus divisores próprios (excluindo ele mesmo). O programa deve imprimir os números perfeitos encontrados na matriz, e também os números que não são perfeitos. O programa deve utilizar a estrutura de decisão if-else para realizar as verificações, e deve permitir que o usuário insira os valores da matriz.
def lemat(mat):
    for l in range (3):
        vet=[]
        for c in range(3):
            v=int(input("Valor: "))
            vet.append(v)
        mat.append(vet)

def teste(m,v1,v2):
    for l in range (3):
        for c in range(3):
            soma=0
            for x  in range(1,m[l][c]):
                if m[l][c]%x==0:
                    soma+=x
            if soma==m[l][c]:
                v1.append(m[l][c])
            else:
                v2.append(m[l][c])

def escreve(v1,v2):
    print(v1)
    print(v2)

    
mat=[]
v1=[]
v2=[]
lemat(mat)
teste(mat,v1,v2)
escreve(v1,v2)


