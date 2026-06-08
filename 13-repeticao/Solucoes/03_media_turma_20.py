# Escreva um programa que leia as notas de 5 alunos em uma turma, e calcule a média de cada aluno. O programa deve permitir que o usuário insira a quantidade de exercícios realizados por cada aluno, e as notas obtidas em cada exercício. O programa deve utilizar a estrutura de repetição for para ler as notas de cada aluno, e a estrutura de decisão if-else para calcular a média. O programa deve imprimir a média de cada aluno para o usuário.
media=[]
soma=0
med=0
l=1
for i in range(5):
    print("Alunos: ",l)
    x=int(input("escreva a quantidade de exercícios realizados: "))
    for j in range (x):
        v=int(input("escreva quanto ele tirou em cada um deles"))
        soma=soma+v
    med=soma/x
    media.append(med)
    l=l+1
    soma=0
    med=0
print("Essa é a lista de notas: ")
for i in range(5):
    print(" ",media[i])
