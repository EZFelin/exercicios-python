# Faça um programa que leia um valor em reais e calcule a menor quantidade de notas e moedas necessárias para representar esse valor. Considere as seguintes denominações: 100, 50, 20, 10, 5, 2 reais e 1 real, 50, 25, 10, 5 e 1 centavos.
valoreais = float(input("Digite o valor em reais: "))
valorcent= int(valoreais * 100)
cem = valorcent // 10000
valorcent%= 10000
cinquenta= valorcent // 5000
valorcent %= 5000
vinte= valorcent // 2000
valorcent%= 2000
dez= valorcent// 1000
valorcent %= 1000
cinco = valorcent // 500
valorcent%= 500
dois = valorcent // 200
valorcent %= 200
real1 = valorcent // 100
valorcent%= 100
cent50 = valorcent // 50
valorcent %= 50
cent25= valorcent // 25
valorcent %= 25
cent10= valorcent // 10


valorcent %= 10
cent5= valorcent // 5
valorcent %= 5
cent1 = valorcent
print(f"o valor em notas de 100 reais é: {cem}")
print(f"o valor em notas de 50 reais e: {cinquenta}")
print(f"o valor em notas de 20 reais é: {vinte}")
print(f"o valor em notas de 10 reais é: {dez}")
print(f"o valor em notas de  5 reais é: {cinco}")
print(f"o valor em notas de  2 reais é: {dois}")
print(f"o valor em moedas de  1 real é: {real1}")
print(f"o valor em moedas de 50 centavos é: {cent50}")
print(f"o valor em moedas de 25 centavos é: {cent25}")
print(f"o valor em moedas de 10 centavos é: {cent10}")
print(f"o valor em moedas de  5 centavos é: {cent5}")
print(f"o valor em moedas de  1 centavo é: {cent1}")










