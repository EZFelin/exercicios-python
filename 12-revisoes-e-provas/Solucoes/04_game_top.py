# O jogo GameTop possui no total 7 fases, em cada fase um jogador pode fazer entre 0 e 5 pontos. Ganha o jogo o jogador que fizer mais pontos, mas para ganhar ele não pode ter 0 pontos em nenhuma fase. Faça um programa em Python que leia e armazene os pontos dos jogadores nas fases do jogo em uma matriz: as linhas contém os pontos dos jogadores em cada fase (as colunas são as fases). Você pode definir a quantidade de jogadores ou ler essa quantidade através de input. Defina funções para: Escrever a matriz com os nomes dos jogadores e seus pontos Escrever se houve um vencedor, e nesse caso informar seu nome e a quantidade de pontos que fez. Se houve empate entre vencedores, escrever seus nomes e a quantidade de pontos que fizeram. Se não houve vencedores (porque todos os jogadores zeraram ao menos uma das fases), escrever o total dos pontos dos jogadores em ordem decrescente de valores.
def escrever_matriz(matriz, nomes):
    print("\nPONTUAÇÕES")

    for i in range(len(matriz)):
        print(nomes[i], end=": ")

        for j in range(7):
            print(matriz[i][j], end=" ")

        print()


def verificar_vencedor(matriz, nomes):
    vencedores = []
    maior = -1

    for i in range(len(matriz)):
        soma = 0
        zerou = False

        for j in range(7):
            soma += matriz[i][j]

            if matriz[i][j] == 0:
                zerou = True

        if not zerou:
            if soma > maior:
                maior = soma
                vencedores = [i]

            elif soma == maior:
                vencedores.append(i)

    if len(vencedores) > 0:
        print("\nVENCEDOR(ES):")

        for indice in vencedores:
            print(nomes[indice], "-", maior, "pontos")

    else:
        print("\nNÃO HOUVE VENCEDOR")

        totais = []

        for i in range(len(matriz)):
            soma = 0

            for j in range(7):
                soma += matriz[i][j]

            totais.append([nomes[i], soma])

        totais.sort(key=lambda x: x[1], reverse=True)

        print("\nPontuações em ordem decrescente:")

        for jogador in totais:
            print(jogador[0], "-", jogador[1], "pontos")


qtd = int(input("Quantidade de jogadores: "))

nomes = []
matriz = []

for i in range(qtd):
    nome = input("\nNome do jogador: ")
    nomes.append(nome)

    linha = []

    print("Digite os pontos das 7 fases:")

    for j in range(7):
        pontos = int(input(f"Fase {j+1}: "))
        linha.append(pontos)

    matriz.append(linha)

escrever_matriz(matriz, nomes)

verificar_vencedor(matriz, nomes)