# Apenas verificar se as notas são maiores que zero.
p1 = float(input("Digite a nota P1: "))
p2 = float(input("Digite a nota P2: "))
t = float(input("Digite a nota T: "))

if p1 > 0 and p2 > 0 and t > 0:
    media = 5 / ((2 / p1) + (1 / p2) + (2 / t))
    print(f"Média = {media:.2f}")
else:
    print("Erro: todas as notas devem ser maiores que zero.")