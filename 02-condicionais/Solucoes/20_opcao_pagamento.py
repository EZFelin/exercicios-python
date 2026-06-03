s=float(input("valor gasto pelo usuário: "))
print("1. À vista no dinheiro 10% de desconto")
print("2. Á vista no cartão de débito 7% de desconto")
print("3. Em uma vez no cartão de crédito: 3% de desconto")
print("4. Em duas ou 3 vezes no cartão de crédito: 1% de desconto")
print("5. Em duas ou 3 vezes no boleto/carnê: 5% de acréscimo")
op=int(input("Qual sua opção? "))
if op==1:
       print("O valor á pagar vai ser de: ",(s-(s*10)/100))
if op==2:
       print("O valor á pagar vai ser de: ",(s-(s*7)/100))
if op==3:
       print("O valor á pagar vai ser de: ",(s-(s*3)/100))
if op==4:
       print("O valor á pagar vai ser de: ",(s-(s*1)/100))
if op==5:
       print("O valor á pagar vai ser de: ",(s-(s*5)/100))
else:
    print("Valor Inválido")
