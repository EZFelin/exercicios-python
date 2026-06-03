# Faça um programa que solicite ao usuário as três notas de um aluno, calcule a média aritmética e classifique a média de acordo com as seguintes categorias:
# 0, se média aritmética (MA) < 6.0;1 se 6.0 <= MA<7.0;2 se 7.0 <= MA < 8.0;3 se 8.0 <= MA < 9.0;4 se MA>=9.0).
nota1=float(input("Digite a nota 1 do aluno (entre 0 e 10)"))
nota2=float(input("Digite a nota 2 do aluno (entre 0 e 10)"))
nota3=float(input("Digite a nota 3 do aluno (entre 0 e 10)"))
ma=((nota1+nota2+nota3)/3)
if ma<6:
    nota_recuperacao=float(input("Digite a nota 4 da prova de recuperação do aluno (entre 0 e 10) "))
    if nota1 <= nota2 and nota1 <= nota3:
        menor_nota = nota1
        nota1 = nota_recuperacao
    elif nota2 <= nota1 and nota2 <= nota3:
        menor_nota = nota2
        nota2 = nota_recuperacao
    else:
        menor_nota = nota3
        nota3=nota_recuperacao
ma=((nota1+nota2+nota3)/3)
if ma<6.0:
    print("0")
elif 6.0<=ma<7.0:
    print("1")
elif 7.0<=ma<8.0:
    print("2")
elif 8.0<=ma<9.0:
    print("3")
else:
    print("4")
