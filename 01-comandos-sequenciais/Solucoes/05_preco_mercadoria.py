# Faça um programa que leia o preço de uma mercadoria e o percentual de desconto. O programa deve calcular e mostrar o valor do desconto e o preço a pagar.
p=int(input("preço da mercadoria: "))
d=int(input("me de o percentual de desconto: "))
v=(p*d)/100
pagar=(p-v)
print("seu valor de desconto foi de: ",v)
print("seu preço a pagar é de: ",pagar)

