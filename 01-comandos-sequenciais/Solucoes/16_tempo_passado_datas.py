# Faça um programa que leia a hora inicial e a hora final de um evento (em horas, minutos e segundos) e calcule o tempo passado entre as duas horas. Considere que o evento pode durar mais de 24 horas.
horai = int(input("Escreva a hora inicial 0-23 hora: "))
minutoi = int(input("Escreva os minutos iniciais 0-59 min: "))
segundoi= int(input("Escreva os segundos iniciais 0-59seg: "))
horaf= int(input("Escreva a hora final 0-23 hora: "))
minutof= int(input("Escreva os minutos finais 0-59 min: "))
segundof= int(input("Escreva os segundos finais 0-59 seg: "))
tempoi = horai* 3600 + minutoi* 60 + segundoi
tempof = horaf* 3600 + minutof* 60 + segundof
tempop= tempof - tempoi
horasp= tempop // 3600
minutosp= (tempop% 3600) // 60
segundosp = tempop% 60
print(f"Tempo passado foi de: {horasp} horas, {minutosp} minutos e {segundosp} segundos.")
