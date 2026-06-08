# Escreva um programa que simule um campeonato de futebol entre duas turmas, a turma da manhã e a turma da tarde. O programa deve permitir que o usuário insira os resultados de 12 jogos entre as duas turmas, onde cada jogo é representado por um placar (gols da turma da manhã e gols da turma da tarde). O programa deve armazenar os resultados em uma lista de listas, onde cada sublista representa um jogo e contém os gols de cada turma. O programa deve então calcular e imprimir as seguintes informações:
# - Qual turma fez mais gols no total
# - Qual jogo teve mais gols
# - Qual turma venceu mais jogos
# - Quantos empates ocorreram
# - Gerar um gráfico de barras mostrando a quantidade de gols de cada turma em cada jogo

def menu():
    print("1) Quem fez mais gols\n")
    print("2) jogo com mais gols")
    print("3) Quem venceu mais jogos\n")
    print("4) quantos empates ocorreram")
    print("5) gerar gráfico\n")
def incluijogos(j):
    import random
    for i in range(12):
        print("Placar do jogo",i+1)
        manha=(random.randint(0,6))
        tarde=(random.randint(0,6))
        #manha=int(input("gols da turma da manha: ")
        #tarde=int(input("gols da turma da tarde: ")
        j.append([manha,tarde])
        
def maisgols(j):
    golstarde=0
    golsmanha=0
    for i in range(12):
        golsmanha=golsmanha+j[i][0]
        golstarde=golstarde+j[i][1]
    if golsmanha>golstarde:
        print("Turma da manha fez mais gols: ",golsmanha)
    if golstarde>golsmanha:
        print("Turma da tarde fez mais gols: ",golstarde)
    else:
        print("empate me gols: ",golsmanha)    


def jogogols(j):
    maisgol=0
    soma=0
    maior=0
    for i in range(12):
        soma=j[i][0] + j[i][1]
        if soma>maior:
            maior=soma
    print("Jogo com mais gols ")
    for i in range(12):
        if maior==j[i][0] + j[i][1]:
            print("Esse(s) jogo(s) tiveram mais gols: ",i+1)
        
def venceumais(j):
    contm=0
    contt=0
    for i in range(12):
        if j[i][0] > j[i][1]:
            contm=contm+1
        elif j[i][0] < j[i][1]:
            contt=contt+1
    if contm > contt:
        print("Manha venceu mais: ",contm)
    elif contt > contm:
         print("Manha venceu mais: ",contt)
    else:
         print("Deu empate: ",contm)




jogos=[]
incluijogos(jogos)
print(jogos)
maisgols(jogos)
jogogols(jogos)
venceumais(jogos)
