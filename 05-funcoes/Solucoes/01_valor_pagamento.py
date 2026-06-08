# Escreva um programa que calcule o valor a ser pago por uma prestação em atraso. O programa deve solicitar o valor da prestação e o número de dias em atraso e apresentar o valor a ser pago. O valor da prestação em atraso é calculado da seguinte forma: para pagamentos sem atraso, cobrar o valor da prestação; quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
def valorpagamento(vp,da):
    if da==0:
        return vp
    else:
        vpag=((vp*3)/100)+((vp*0.1)/100)*da+vp
        return vpag

valor=float(input("Valor da prestação: "))
diasatraso=int(input("Dias em atraso: "))
vt=0
quant=0
while valor!=0:
    vp=(valorpagamento(valor,diasatraso))
    print(vp)
    vt=vt+vp
    valor=float(input("Valor da prestação: "))
    diasatraso=int(input("Dias em atraso: "))
    quant=quant+1
print(f"Esse é o total pago: R${vt:.2f}")
print("Esse é a quantidade de parcelas: ",quant)
