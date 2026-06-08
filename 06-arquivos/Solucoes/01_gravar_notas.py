# Escreva um programa que leia o nome e as notas de 20 alunos, calcule a média de cada aluno e grave os dados em um arquivo CSV. O programa deve solicitar ao usuário a média mínima para aprovação e, em seguida, imprimir uma mensagem indicando se cada aluno foi aprovado ou reprovado com base na média calculada.
arq = open('notas13.csv', 'a')
media=float(input("Digite a média para ser aprovado: "))
if media<0 or media>10:
    print("Número inválido! media<0 ou media >10")
    media=float(input("Digite a média para ser aprovado: "))
x=1
while x<=20:
    nomes=input("Escreva o nome do aluno: ")
    nota1=float(input("Digite a nota 1: "))
    nota2=float(input("Digite a nota 2: "))
    if (nota1<0 or nota1>10)and(nota2<0 or nota2>10):
        print("Número Inválido! nota<0 ou nota>10")
        nota1=float(input("Digite a nota 1: "))
        nota2=float(input("Digite a nota 2: "))
    median=(nota1+nota2)/2
    arq.write(nomes+";"+str(nota1)+";"+str(nota2)+"\n")
    if median>=media:
        print("O aluno:",nomes," Foi aprovado!","com a média de: ",median)
    else:
        print("O aluno:",nomes,"Foi reprovado!","com a média de: ",median)
    x=x+1
arq.close()
