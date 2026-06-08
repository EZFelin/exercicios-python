# Escreva um programa que leia as notas de 6 alunos em 3 avaliações, calcule a média de cada aluno e a média de cada avaliação, e imprima os resultados. O programa deve utilizar listas para armazenar as notas e as médias, e deve utilizar a biblioteca Matplotlib para criar gráficos de barras mostrando a média de cada aluno e a média de cada avaliação.
import matplotlib.pyplot as plt
n1 = []
n2 = []
n3 = []
meda = []
medn = []


for i in range(6):
    print(f"Aluno {i+1}:")
    not1 = float(input("Digite a primeira nota: "))
    not2 = float(input("Digite a segunda nota: "))
    not3 = float(input("Digite a terceira nota: "))


    n1.append(not1)
    n2.append(not2)
    n3.append(not3)


    media_a = (not1 + not2 + not3) / 3
    meda.append(media_a)


med1 = sum(n1) / 6
med2 = sum(n2) / 6
med3 = sum(n3) / 6


mednot = [med1, med2, med3]


print("\nNotas dos alunos:")
print("Notas 1:", n1)
print("Notas 2:", n2)
print("Notas 3:", n3)
print("\nMédias dos alunos:", meda)
print("Médias das notas:", medn)


plt.figure(figsize=(10, 5))


plt.subplot(1, 2, 1)
plt.bar([f'Aluno {i+1}' for i in range(6)], meda, color='blue')
plt.title('Média de cada Aluno')
plt.xlabel('Alunos')
plt.ylabel('Média')


plt.subplot(1, 2, 2)
plt.plot(['Nota 1', 'Nota 2', 'Nota 3'], medn, marker='o', color='yellow')
plt.title('Média de cada Nota')
plt.xlabel('Notas')
plt.ylabel('Média')


plt.tight_layout()
plt.show()


