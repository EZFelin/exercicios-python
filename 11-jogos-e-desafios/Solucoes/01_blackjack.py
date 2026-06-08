# Escreva um programa que simule um jogo de Blackjack entre dois jogadores. O programa deve gerar aleatoriamente dois números entre 1 e 10 para cada jogador, e calcular a soma desses números. O jogador que tiver a soma mais próxima de 21 sem ultrapassá-lo vence o jogo. O programa deve permitir que cada jogador escolha se deseja pegar mais uma carta (gerar outro número aleatório) ou se deseja ficar com a soma atual. O programa deve continuar permitindo que os jogadores peguem cartas até que um deles ultrapasse 21 ou decida ficar com a soma atual. Ao final do jogo, o programa deve imprimir o resultado, indicando qual jogador venceu ou se houve empate.
import random
x1=(random.randint(1,10))
y1=(random.randint(1,10))
x2=(random.randint(1,10))
y2=(random.randint(1,10))
x=x1+x2
y=y1+y2
print("Os números do jogador x é: ",x1,x2,"Sua soma é: ",x1+x2)
print("Os números do jogador y é: ",y1,y2,"Sua soma é: ",y1+y2)
j1=str(input("jogador x você deseja pegar mais uma carta?(s ou n)"))
while j1=='s':
    x3=(random.randint(1,10))
    x=x+x3
    print("Numero do jogador 1: ",x)
    if x>=21:
        break
    else:
        j1=str(input("jogador x você deseja pegar mais uma carta?(s ou n)"))
print("Nùmero do jogador: ",y)
j2=str(input("jogador y você deseja pegar mais uma carta?(s ou n)"))
while j2=='s':
    y3=(random.randint(1,10))
    y=y+y3
    print("Voce tirou: ",y)
    if y>=21:
        break
    else:
        j2=str(input("jogador y você deseja pegar mais uma carta?(s ou n)"))

    if x==y:
            print("O jogo empatou.")
    elif x<21 and y<21:
        if x>y:
            print("O jogador 1 ganhou!")
            print("O número do jogador 1 é ",x," e o do jogador 2 é ",y)
    else:
            print("O jogador 2 ganhou!")
            print("O número do jogador 1 é ",x," e o do jogador 2 é ",y)
    if x>21 and y<=21:
            print("O jogador 2 venceu.")
            print("O número do jogador 1 é ",x," e o do jogador 2 é ",y)
    elif x<=21 and y>21:
            print("O jogador 1 venceu.")
            print("O número do jogador 1 é ",x," e o do jogador 2 é ",y)