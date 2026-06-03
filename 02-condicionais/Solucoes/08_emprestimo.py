# Faça um programa que solicite ao usuário o valor de uma casa, o salário de quem vai comprar e a quantidade de anos para pagar. Calcule o valor da prestação mensal e verifique se ela é inferior ou igual a 30% do salário. Se for, o empréstimo pode ser concedido; caso contrário, ele deve ser negado.
a=float(input("Valor da casa: "))
b=float(input("Valor do salário de quem vai comprar: "))
c=float(input("Quantidade de anos que vai fazer pagamento: "))
meses=(c*12)/a
sa=(b*30)/100
if sa>b:
    print("Empréstimo não concedido")
if sa<b or sa==b:
    print("O valor da prestação que irá pagar é de: ",a/c)
