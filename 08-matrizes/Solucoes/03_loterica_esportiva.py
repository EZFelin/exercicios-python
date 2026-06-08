# Escreva um programa que simule uma loteria esportiva, onde o usuário deve escolher entre 1, 2 ou 3 para cada um dos 13 jogos. O programa deve ler o gabarito dos jogos (as respostas corretas) e as apostas do usuário, armazenando essas informações em matrizes. Em seguida, o programa deve comparar as apostas do usuário com o gabarito e calcular a quantidade de pontos obtidos, bem como o percentual de acertos. O programa também deve contar quantas apostas simples, duplas e triplas foram feitas pelo usuário e imprimir esses resultados. Por fim, o programa deve permitir que o usuário escolha entre realizar uma nova aposta ou encerrar o programa.
vet=[]
def gabarito():
    print("""1-Coluna um.
2-Coluna do meio.
3-Coluna dois.""")
    for j in range(13):
        n=int(input("Digite o gabarito dos jogos: "))
        if n<1 or n>3:
            n=int(input("Opção inválida. Digite novamente: "))
        vet.append(n)


v=[]
m=[]
quant=0
quantap1=0
quantap2=0
quantap3=0
def aposta():
    print("""1-Apostas simples(uma vez)
2-Apostas duplas(duas vezes)
3-Apostas triplas(três vezes)""")
    for l in range(13):
        quantap=int(input("Escreva o tipo de apostas escolhido: "))
        print("""1-Aposta na vitória do time A.
2-Aposta no empate.
3-Aposta na vitória do time B.""")
        if quantap==1:
            ap=int(input("Digite a sua aposta: "))
            if ap!=1 and ap!=2 and ap!=3:
                ap=int(input("Opção inválida. Digite novamente: "))
            for c in range(3):
                if ap==c+1:
                    v.append(1)
                else:
                    v.append(0)
            quantap1+=1
        elif quantap==2:
            ap1=int(input("Digite a sua primeira aposta: "))
            if ap1!=1 and ap1!=2 and ap1!=3:
                ap1=int(input("Opção inválida. Digite novamente: "))
            ap2=int(input("Digite a sua segunda aposta: "))
            if ap2!=1 and ap2!=2 and ap2!=3:
                ap2=int(input("Opção inválida. Digite novamente: "))
            for c in range(3):
                if ap1==c+1 or ap2==c+1:
                    v.append(1)
                else:
                    v.append(0)
            quantap2+=1
        elif quantap==3:
            for c in range(3):
                v.append(1)
            print("Apostas feitas.")
            quantap3+=1
        else:
            quantap=int(input("Opção inválida. Digite novamente: "))
        for j in range(3):
            if v[j]==0:
                quant+=1
        m.append(v)
pontos=0
def calcular():
    for l in range(13):
            for c in range(3):
                if m[l][c]==v[l]:
                    pontos+=1
    percent=(100*pontos)/13
    print("A quantidade de pontos obtidos é ",pontos," e o percentual de acertos é ",percent,"%")


def numerap():
    print("Número de apostas simples: ",quantap1)
    print("Número de apostas duplas: ",quantap2)
    print("Número de apostas triplas: ",quantap3)
    
op=0    
while op!=5:    
    op=int(input("n= "))
    if op==1:
        op1=gabarito()
    elif op==2:
        op2=aposta()
    elif op==3:
        op3=calcular()
    elif op==4:
        op4=numerap()
    elif op==5:
        print("Programa encerrado.")