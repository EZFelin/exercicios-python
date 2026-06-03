# Faça um programa que solicite ao usuário a hora de início e a hora de término de um jogo de futebol, considerando que o jogo pode começar e terminar no mesmo dia. Calcule a duração do jogo em horas e minutos. Considere os seguintes critérios para validar as horas:
# - As horas devem ser um número entre 0 e 23.
hi=int(input("Digite a hora inicial: "))
mi=int(input("Digite o minuto inicial : "))
hf=int(input("Digite a hora final: "))
mf=int(input("Digite o minuto final: "))
if hi>=0 and hi<=23 and mi>=0 and mi<=59 and hf>=0 and hf<=23 and mf>=0 and mf<=59:
    print("A quantidade de horas jogadas é de: ",(hf-hi),"horas",(mf-mi),"minutos")
else:
    print("Valor inválido")
