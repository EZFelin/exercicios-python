#Considere que um fumante perde 10 minutos de vida a cada cigarro. exiba o total em dias.
quant=int(input("Escreva a quantidade de cigarros que o fumante fuma por dia: "))
anos=int(input("Escreva por quantos anos o fumante fuma: "))
perder=(quant*10)*(365*anos)/1440
print ("total de dias que o fumante perdeu: ",perder)
