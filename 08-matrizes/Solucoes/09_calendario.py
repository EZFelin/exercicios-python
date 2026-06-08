# Escreva um programa que leia o dia do mês (D) e o dia da semana (DS) do primeiro dia do mês, e gere uma matriz de 6 linhas e 7 colunas representando um calendário mensal. A matriz deve ser preenchida com os números dos dias do mês, começando pelo dia D na posição correspondente ao dia da semana DS. Os dias anteriores a D devem ser preenchidos com zeros, e os dias posteriores a 30 também devem ser preenchidos com zeros. O programa deve imprimir a matriz resultante, representando o calendário do mês.
def calendario(D, DS):
    # Inicializa a matriz Folhinha com zeros
    Folhinha = [[0 for _ in range(7)] for _ in range(6)]
    
    # Calcula o dia da semana do primeiro dia do mês
    primeiro_dia_semana = (DS - (D % 7) + 1) % 7
    if primeiro_dia_semana == 0:
        primeiro_dia_semana = 7

    # Preenche a matriz com os dias do mês
    dia = 1
    for semana in range(6):
        for dia_semana in range(7):
            if semana == 0 and dia_semana < primeiro_dia_semana - 1:
                continue
            if dia > 30:
                break
            Folhinha[semana][dia_semana] = dia
            dia += 1

    return Folhinha

def imprimir(Folhinha):
    for semana in Folhinha:
        print(semana)

# Leitura dos valores D e DS
D = int(input("Digite o dia do mês (1-30): "))
if D<0 or D>30:
    D = int(input("Numero invalido! Digite o dia do mês novamente (1-30): "))
DS = int(input("Digite o dia da semana (1-domingo, 2-segunda, 3-terça, 4-quarta, 5- quinta,6-sexta, 7-sábado): "))

# Geração e impressão do calendário
Folhinha = calendario(D, DS)
imprimir(Folhinha)
