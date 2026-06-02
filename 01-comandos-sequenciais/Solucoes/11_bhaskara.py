# Faça um programa que leia os coeficientes a, b e c de uma equação do segundo grau (ax^2 + bx + c = 0) e calcule as raízes da equação usando a fórmula de Bhaskara. O programa deve mostrar as raízes com duas casas decimais e a soma das raízes com três casas decimais.
import math
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
delta=(b**2)-(4*a*c)
#res=delta**(1/2)
res=math.sqrt(delta)
x1=(-b+res)/(2*a)
x2=(-b-res)/(2*a)
print(f"x1={x1:.2f}")
print(f"x2={x2:.2f}")
print(f"soma={x1+x2:.3f}")
