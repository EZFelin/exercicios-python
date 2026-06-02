# Faça um programa que leia a distância em km e a velocidade média em km/h de uma viagem e calcule o tempo necessário para realizá-la, mostrando o resultado em minutos.
distancia=int(input("Escreva a distancia em km: "))
vmedia=int(input("Escreva a velocidade média em km/h: "))
l=(distancia/vmedia)*60

print ("o tempo de viagem é de {:.1f} minutos." .format (l))