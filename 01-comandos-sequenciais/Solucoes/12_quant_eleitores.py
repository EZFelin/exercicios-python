# Faça um programa que leia o número total de eleitores de um município, o número de votos em branco, nulos e válidos. O programa deve calcular e mostrar o percentual que cada um representa em relação ao total de eleitores.
total=int(input("Escreva o número total de eleitores: "))
branco=int(input("Escreva o número de votos em branco: "))
nulos=int(input("Escreva o número de votos em nulo: "))
validos=int(input("Escreva o número de votos válidos: "))
m=(100*branco)/total
n=(100*nulos)/total
o=(100*validos)/total
print(f"O percentual de votos em branco é de {m:,.0f}%")
print(f"O percentual de votos em nulos é de {n:,.0f}%")
print(f"O percentual de votos válidos é de {o:,.0f}%")
