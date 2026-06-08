# Escreva um programa que leia os 9 primeiros dígitos de um CPF, e calcule os dois dígitos verificadores do CPF. O programa deve utilizar a estrutura de repetição for para ler os dígitos, e a estrutura de decisão if-else para calcular os dígitos verificadores. O programa deve imprimir os dígitos verificadores para o usuário.
c1=0
c2=0
d1=0
d2=0
for i in range(10,1,-1):
	d=int(input("Digito:"))
	c1=c1+i*d
	c2=c2+(i+1)*d
r1=c1%11
if r1<=1:
	d1=9
else:
	d1=11-r1
c2=c2+2*d1
r2=c2%11

if r2 <=1:
    d2=0
else:
    d2=11-r2
    print("d1=",d1)
    print("d2=",d2)
