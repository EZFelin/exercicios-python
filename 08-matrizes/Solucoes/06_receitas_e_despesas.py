# Escreva um programa que leia uma matriz de 2 linhas e 3 colunas, preenchida pelo usuário, representando as receitas e despesas de uma pessoa em dois dias. A primeira coluna deve conter a receita do dia, enquanto as outras duas colunas devem conter os gastos do dia. O programa deve calcular o saldo de cada dia (receita menos despesas) e determinar se a pessoa ficou com saldo positivo ou negativo em cada dia. Além disso, o programa deve calcular a média das receitas e despesas para cada coluna e imprimir os resultados.
def positivo(mat):
    soma=0
    for l in range(2):
        for c in range(3):
            if c>0:
                soma=soma+mat[l][c]
        if soma<mat[l][0]:
            print("No dia,",l+1,",ficou positivo.")
        soma=0
        
def media(mat,n):
    soma=0
    for l in range(2):
        for c in range(3):
            if c==n:
                soma=soma+mat[l][c]
    return soma/2
            
mat=[]
vet=[]
for l in range(2):
    print("Dia: ",l+1)
    for c in range(3):
            n=float(input("Escreva a receita, e seus 2 gastos: "))
            vet.append(n)
    mat.append(vet)
    vet=[]


print("Esses são os que ficaram com a receita positiva: ")
positivo(mat)
n=int(input("Escreva qual coluna deseja saber(1-tal,2-tel)"))
print("Essa é a média,",media(mat,n))




