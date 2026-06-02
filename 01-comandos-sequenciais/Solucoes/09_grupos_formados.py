# Faça um programa que leia a quantidade de alunos em uma sala e a quantidade de alunos por grupo. O programa deve calcular quantos grupos podem ser formados e quantos alunos sobrariam para formar um grupo completo.
sala=int(input("Escreva a quantidade de alunos na sala: "))
grupo=int(input("Escreva a quantidade de alunos por grupo: "))
gformados=(sala//grupo)
resto=(sala%grupo)
print("a quantidade de grupos formados é de: ",gformados)
print("o resto de alunos que não foram suficientes é de: ",resto)
