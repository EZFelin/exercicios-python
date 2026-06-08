# Escreva um programa que simule um jogo da velha. O programa deve ler o estado atual do jogo, representado por uma matriz de 3x3, onde cada posição pode conter um valor 0 (indica que a posição está vazia), 1 (indica que o jogador 1 marcou a posição) ou 2 (indica que o jogador 2 marcou a posição). O programa deve determinar se há um vencedor (jogador 1 ou jogador 2) ou se o jogo está empatado. O programa deve verificar as linhas, colunas e diagonais da matriz para identificar o vencedor. Se houver um vencedor, o programa deve imprimir qual jogador venceu. Se o jogo estiver empatado, o programa deve imprimir "Empate". Se o jogo ainda não terminou (ou seja, há posições vazias e nenhum vencedor), o programa deve imprimir "O jogo ainda não terminou".
def vencedor():
    #linhas
    somacol1=0
    somalin2=0
    somalin1=0
    somacol2=0
    
    for l in range (3):
        for c in range(3):
            if mat[l][0]==mat[l][1]==mat[l][2]==1 :
                somalin1=somalin1+1
            if mat[l][0]==mat[l][1]==mat[l][2]==2 :
                somalin2=somalin2+1
   
    if somalin1==3:
        print("Jogador 1 Venceu!Com linha.")
    elif somalin2==3:
        print("Jogador 2 Venceu!Com linha.")
        
    #colunas
    for c in range(3):
        for l in range (3):
            if mat[0][c]==mat[1][c]==mat[2][c]==1 :
                somacol1=somacol1+1
            if mat[0][c]==mat[1][c]==mat[2][c]==2 :
                somacol2=somacol2+1
                
    if somacol1==3:
        print("Jogador 1 Vencedor!Com coluna.")
    elif somacol2==3:
        print("Jogador 2 Vencedor!Com coluna.")
        
    #diagonais
    if mat[0][0]==mat[1][1]==mat[2][2]==1 or mat[0][2]==mat[1][1]==mat[2][0]==1:
        print("Jogador 1 Vencedor!Com diagonal.")
    elif mat[0][0]==mat[1][1]==mat[2][2]==2 or mat[0][2]==mat[1][1]==mat[2][0]==2:
        print("Jogador 2 Vencedor!Com diagonal.")
        
    #empate
    for linha in mat:
         if 0 in linha:
           print("O jogo ainda não terminou.")
   
    print("Empate!")


mat=[]
vet=[]
print("0-para incompleto,1- para jogador 1,2- para jogador 2")
for l in range (3):
    for c in range(3):
        n=int(input("Escreva como está o jogo da velha ["+str(l)+"]["+str(c)+"]:"))
        vet.append(n)
    mat.append(vet)
    vet=[]
vencedor()
