# Escreva um programa que leia a área total de uma obra (em m²) e calcule quantos dias serão necessários para concluir a obra, considerando que cada operário consegue produzir 0,9 m² por dia. O programa deve calcular o número de dias necessários para concluir a obra com 1 operário, 2 operários, 3 operários, e assim por diante, até que o número de dias seja menor ou igual a 1. O programa deve imprimir o número de operários e o número de dias necessários para concluir a obra para cada caso, e deve utilizar a biblioteca Matplotlib para criar um gráfico mostrando a relação entre o número de operários e o número de dias necessários para concluir a obra.
import matplotlib.pyplot as plt

area_total= float(input("Digite a área total da obra (em m²): "))

prodop = 0.9


nope = []
diasn = []


op = 1
while True:
    dias = area_total / (op * prodop)
   
    nope.append(op)
    diasn.append(dias)
   
    if dias <= 1:
        break
   
    op+= 1


for i in range(len(nope)):
    print(f"Operários: {nope[i]}, Dias: {diasn[i]:.2f}")


plt.plot(nope, diasn, marker='o', color='green')
plt.title('Dias Necessários para Concluir a Obra')
plt.xlabel('Número de Operários')
plt.ylabel('Dias Necessários')
plt.grid(True)
plt.show()

