# Faça um programa que solicite ao usuário a distância de uma viagem em quilômetros e calcule o preço da passagem de acordo com as seguintes regras:
# - Para viagens de até 200 km, o preço é de R$ 0,50 por km.
# - Para viagens acima de 200 km, o preço é de R$ 0,45 por km. 
distancia = float(input("Digite a distância da viagem em km: "))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f"Valor da passagem: R$ {preco:.2f}")