# Escreva um programa que simule um jogo de RPG entre um personagem controlado pelo usuário e um inimigo controlado pelo computador. O programa deve permitir que o usuário escolha o nome do personagem, o nome do inimigo, a arma do personagem e a arma do inimigo. O programa deve gerar aleatoriamente a vida inicial do personagem e do inimigo, e permitir que o usuário escolha entre três tipos de ataques (chutar, bater ou usar a arma) para atacar o inimigo. O programa deve calcular o dano causado por cada ataque e atualizar a vida do personagem e do inimigo de acordo. O programa deve continuar permitindo que o usuário ataque até que a vida de um dos personagens chegue a zero ou menos, momento em que o programa deve imprimir o resultado do jogo (vitória ou derrota). O programa deve utilizar a biblioteca random para gerar os valores aleatórios de vida e dano dos ataques.
nomep=str(input("Escreva o nome do seu personagem: "))
nomej=str(input("Escreva o seu nome: "))
nomei=str(input("Escreva o nome do seu inimigo: "))
armaj=str(input("Escreva o nome da sua arma: "))
armai=str(input("Escreva o nome da arma do inimigo: "))
import random
vs=(random.randint(15,30))
vi=(random.randint(15,30))
print("\nSua vida é de: ",vs)
print("A vida de seu inimigo é: ",vi)
while vs>=0 and vi>=0:
    print("\n você tem 3 tipos de ataques, escolha:",
           "1- Chutar 2- Bater 3- Usar sua arma")
    bh=int(input("Digite o número de sua escolha: "))
    if bh==1:
           chutar=random.randint(1,6)
           print("\n",nomep," Atacou dando sua bicuda mortal e tirou ",chutar," de HP de ",nomei)
           vi=vi-chutar
    elif bh==2:
           bater=random.randint(1,8)
           print("\n",nomep," Atacou dando um soco mortal e tirou ",bater," de HP de ",nomei)
           vi=vi-bater
    else:
        usararma=random.randint(1,10)
        print("\n",nomep," Atacou dando um soco mortal e tirou ",usararma," de HP de ",nomei)
        vi=vi-usararma
    attki=random.randint(1,3)
    if attki==1:
           chutar=random.randint(1,6)
           print("\n",nomei," Atacou dando sua bicuda mortal e tirou ",chutar," de HP de ",nomep)
           vs=vs-chutar
    elif attki==2:
           bater=random.randint(1,8)
           print("\n",nomei," Atacou dando um soco mortal e tirou ",bater," de HP de ",nomep)
           vs=vs-bater
    else:
        usararma=random.randint(1,10)
        print("\n",nomei," Atacou dando um soco mortal e tirou ",usararma," de HP de ",nomep)
        vs=vs-usararma
        
if vs>=0:
    print("\nVocê Venceu!!")
else:
    print("\nGAME OVER")
