# Escreva um programa que leia uma matriz de 3 linhas e 3 colunas, preenchida pelo usuário, e calcule a soma dos valores da linha 2, da coluna 3, da diagonal principal, da diagonal secundária, de todos os valores da matriz, de cada linha e de cada coluna. O programa deve imprimir os resultados dessas somas.
m1=[]
m2=[]
for j in range (3):
    for i in range(3):
        n=int(input("Escreva números: ["+str(i)+"]["+str(j)+"]"))
        m1.append(n)
    m2.append(m1)
    m1=[]

soma2=0
for j in range (3):
    for i in range(3):
        if j==1:
            soma2=soma2+m2[i][j]
soma3=0          
for j in range (3):
    for i in range(3):
        if i==2:
            soma3=soma3+m2[i][j]
somaprin=0
for j in range (3):
    for i in range(3):
        if i==j:
            somaprin=somaprin+m2[i][j]
x=0
y=2
somasecun=0
for j in range (3):
    for i in range(3):
        if j==x and i==y and m2[i][j]>0:
            somasecun=somasecun+m2[i][j]
    x=x+1
    y=y-1
somatotal=0
for j in range (3):
    for i in range(3):
        somatotal=somatotal+m2[i][j]
somalin=0
for j in range (3):
    for i in range(3):
        if i==m2[i][j]:
            somalin=somalin+m2[i][j]
somacol=0
for j in range (3):
    for i in range(3):
        if j==m2[i][j]:
            somacol=somacol+m2[i][j]

for j in range (3):
    print("\n")
    for i in range(3):            
        print(m2[i][j]," ")
    
print("Essa é a soma dos valores da linha 2 de m: ",soma2)
print("Essa é a soma dos valores da coluna 3 de m: ",soma3)
print("Essa é a soma dos valores da diagonal principal: ",somaprin)
print("Essa é a soma dos valores da diagonal secundária: ",somasecun)
print("Essa é a soma de todos os valores da matriz: ",somatotal)
print("Essa é a soma dos valores de cada linha da matriz: ",somalin)
print("Essa é a soma dos valores de cada coluna da matriz: ",somacol)

