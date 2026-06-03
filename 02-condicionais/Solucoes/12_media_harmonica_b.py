# Verificar se as notas estão entre 0.1 e 10
p1 = float(input("Digite a nota P1: "))
p2 = float(input("Digite a nota P2: "))
t = float(input("Digite a nota T: "))

if 0.1 <= p1 <= 10 and 0.1 <= p2 <= 10 and 0.1 <= t <= 10:
    media = 5 / ((2 / p1) + (1 / p2) + (2 / t))
    print(f"Média = {media:.2f}")
else:
    print("Erro: as notas devem estar entre 0.1 e 10.")