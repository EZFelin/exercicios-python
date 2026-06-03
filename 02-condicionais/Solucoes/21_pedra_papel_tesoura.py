import random
x=(random.randint(1,3))
print("1. Pedra")
print("2. Papel")
print("3. Tesoura")
a=int(input("Você está no jogo da PEDRA,PAPEL,TESOURA! Escolha sua jogada: "))
if a==x:
    print("Empate")
elif x==1 and a==2:
    print("Você ganhou!!!!!!!!!!!!!!")
elif x==2 and a==3:
    print("Você ganhou!!!!!!!!!!!!!!")
elif x==3 and a==1:
    print("Você ganhou!!!!!!!!!!!!!!")
elif x==2 and a==1:
    print("Você perdeu :(")
elif x==3 and a==2:
    print("Você perdeu :(")
elif x==1 and a==3:
    print("Você perdeu :(")
