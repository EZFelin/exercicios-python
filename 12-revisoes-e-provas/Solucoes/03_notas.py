# Escreva um programa que leia as notas de 10 estudantes em três disciplinas (programação I, algoritmos e suporte e redes I), e armazene as notas em uma matriz. O programa deve então apresentar um menu de opções para o usuário, onde ele pode escolher entre as seguintes opções:
# 1) Zero total: Retorna a quantidade de estudantes que zeraram as provas em todas as disciplinas.
# 2) Zero disciplina: Retorna a quantidade de estudantes que zeraram as provas em uma disciplina específica, e qual é essa disciplina.
# 3) Dois zeros: Retorna a quantidade de estudantes que zeraram as provas em    duas disciplinas, e quais são essas disciplinas.
# 4) Três zeros: Retorna a quantidade de estudantes que zeraram as provas   em todas as três disciplinas, e o código do estudante.
# 5) Média: Retorna a média aritmética de cada estudante considerando as três disciplinas.
# 6) Média mais alta: Retorna a média mais alta entre os estudantes considerando as três disciplinas.
# 7) Sair: Encerra o programa. O programa deve utilizar a estrutura de decisão if-elif-else para realizar as verificações, e deve permitir que o usuário escolha as opções do menu repetidamente até que ele escolha encerrar o programa.
#Revisão
def menu():
    print("(1)Zero total: Zero em todas as materias."
          "(2)Zero disciplina: Zero na disciplina."
          "(3)Dois zeros: Zero em 2 disciplinas e quais sao elas."
          "(4)Tres zeros: Zero nas tres disciplias e codigo estudante."
          "(5)Media: Escreve as médias aritméticas de cada estudante."
          "(6)Media mais alta: Retorna a media mais alta considerando as 3 disciplinas."
          "(7)Sair")
def zerototal(m):
    quant=0
    for l in range(3):
        for c in range(10):
            if m[l][c]==0:
                quant=quant+1
    return quant


def zerodisciplina(m):
    print("1)programação I 2)algoritmos 3)suporte e redes I ")
    d=int(input("Escreva a matéria que deseja saber: "))
    quant=0
    for c in range(10):
        if d==1:
            if m[0][c]==0:
                quant=quant+1
        if d==2:
            if m[1][c]==0:
                quant=quant+1
        if d==3:
            if m[2][c]==0:
                quant=quant+1
    return quant


def doiszeros(m,vet):
    for c in range(10):
        quant=0
        vet=[]
        if m[0][c]==0:
            quant+=1
            vet.append("Programação")
        if m[1][c]==0:
            quant+=1
            vet.append("Algoritmo")
        if m[2][c]==0:
            quant+=1
            vet.append("Suportes e redes")
        if quant==2:
            print("\nO estudante:",c," tem zero em duas disciplinas.")
            print("Essas são as disciplinas: ",vet,"\n")


def treszeros(m):
      for c in range(10):
        if m[0][c]==0 and m[1][c]==0 and m[2][c]==0:
            print("Esse é o código do estudante que zerou as provas: ",c)


def media(m):
    soma=0
    for l in range(3):
        for c in range(10):
            soma=soma+m[l][c]
        print("O Aluno: ",c," teve a média de: ",soma/3)
        soma=0


def mediamaisalta(m):
    mais=m[0][0]
    soma=0
    for c in range(10):
        soma=0
        for l in range(3):
            soma+=m[l][c]
        med=soma/3
        if med>mais:
            mais=med
    return mais
        
#vet=[]
pro=[0,0,0,4,6,8,5,0,8,0]
alg=[0,0,9,8,7,6,7,8,6,5]
sup=[0,7,6,4,5,6,7,5,0,5]
m=[pro,alg,sup]
vetor=[]
#print("1)programação I 2)algoritmos 3)suporte e redes I")
#for l in range(3):
#    print("escreva a nota da disciplina: ",l+1)
#    for c in range(10):
#        n=float(input("\n(0-10)Nota: "))
#        vet.append(n)
#   m.append(vet)
#   vet=[]


op=0
while op!=7:
    menu()
    op=int(input("Escreva sua opção: "))
    if op==1:
        zerot=zerototal(m)
        print("Esse é o total de zeros: ",zerot)
    elif op==2:
        zerod=zerodisciplina(m)
        print("Esse é o total de zeros na disciplina: ",zerod)
    elif op==3:
        doiszeros(m,vetor)
    elif op==4:
        treszeros(m)
    elif op==5:
        media(m)
    elif op==6:
        mediaalta=mediamaisalta(m)
        print("Essa é a média mais alta: ",mediaalta)
    elif op==7:
        print("Muito obrigado por usar o programa!")