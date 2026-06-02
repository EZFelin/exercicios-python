# Faça um programa que leia a altura e o raio de um tanque cilíndrico e calcule a quantidade de latas de tinta necessárias para pintar o tanque, sabendo que cada lata de tinta tem 5 litros e cada litro pinta 3 metros quadrados. O programa deve também calcular o custo total para pintar o tanque, considerando que cada lata de tinta custa R$ 40,00.
altura = float(input("Escreva  a altura do cilindro em metros: "))
raio = float(input("Escreva o raio do cilindro em metros: "))
areatotal = (2 * 3.14 * raio**2) + (2 * 3.14 * raio * altura)
litrostinta = areatotal / 3  
latastinta = litrostinta / 5  
custototal = latastinta * 40.00
print(f"a quantidade de latas de tinta em que eram precisas eram de: {latastinta:.2f}")
print(f"o valor total para pintar o tanque cilíndrico foi de: R$ {custototal:.2f}")
