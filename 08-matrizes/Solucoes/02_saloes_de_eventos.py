# Escreva um programa que leia uma matriz de 4 linhas e 3 colunas, preenchida pelo usuário, representando a quantidade de equipamentos disponíveis em um salão de eventos para cada dia da semana (sexta, sábado e domingo). O programa deve calcular a soma dos equipamentos para cada dia da semana e determinar qual dia tem a maior quantidade de equipamentos disponíveis. Por fim, o programa deve imprimir a matriz original, as somas dos equipamentos para cada dia e o dia com a maior quantidade de equipamentos.
mat=[]
vet=[]
somalinhas=[]
somacolunas=[]
for l in range (4):
    for c in range(3):
        n=int(input("Escreva a quantidade de equipamentos: ["+str(l)+"]["+str(c)+"]"))
        vet.append(n)
    mat.append(vet)
    vet=[]
somasex=0
d=input("escreva um dia(sexta,sabado,domingo): ")
if d=='sexta':
    for l in range (4):
        for c in range(3):
            if c==0:
                somasex=somasex+mat[l][c]
    print("Esse é o total de itens na sexta: ",somasex)
somasab=0
if d=='sabado':
    for l in range (4):
        for c in range(3):
            if c==1:
                somasab=somasab+mat[l][c]
    print("Esse é o total de itens na sexta: ",somasab)
somadom=0
if d=='domingo':
    for l in range (4):
        for c in range(3):
            if c==2:
                somadom=somadom+mat[l][c]
    print("Esse é o total de itens na sexta: ",somadom)


if somasex<somasab or somasex<somadom:
    print("Sexta tem mais equipamentos!")
elif somasab<somasex or somasab<somadom:
    print("Sábado tem mais equipamentos!")
elif somadom<somasab or somadom<somasex:
    print("Domingo tem mais equipamentos!")
