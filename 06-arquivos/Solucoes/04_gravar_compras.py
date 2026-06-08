# Escreva um programa que leia o nome e o valor de uma compra, solicite a forma de pagamento e calcule o valor total a pagar com base nas seguintes condições:
# 1. À vista no dinheiro: 10% de desconto
# 2. Á vista no cartão de débito: 7% de desconto
# 3. Em uma vez no cartão de crédito: 3% de desconto
# 4. Em duas ou 3 vezes no cartão de crédito: 1% de desconto
# 5. Em duas ou 3 vezes no boleto/carnê: 5% de acréscimo
# O programa deve gravar os dados da compra em um arquivo de texto, incluindo o nome
nome=str(input("Escreva seu nome: "))
vpagar=float(input("Digite o valor da compra: "))
print("Formas de Pagamento:")           
print("1. À vista no dinheiro 10% de desconto")
print("2. Á vista no cartão de débito 7% de desconto")
print("3. Em uma vez no cartão de crédito: 3% de desconto")
print("4. Em duas ou 3 vezes no cartão de crédito: 1% de desconto")
print("5. Em duas ou 3 vezes no boleto/carnê: 5% de acréscimo")
print("6. Ver relatório de compra")
opcao=int(input("Digite a forma de pagamento: "))
if opcao==1:
        d=(vpagar*10)/100
        vtotal=vpagar-d
        print("O total a pagar é: ",vtotal)
elif opcao==2:
        d=(vpagar*7)/100
        vtotal=vpagar-d
        print("O total a pagar é: " + str(vtotal))
elif opcao==3:
        d=(vpagar*10)/100
        vtotal=vpagar-d
        print("O total a pagar é: ",vtotal)
elif opcao==4:
        d=(vpagar*1)/100
        vtotal=vpagar-d
        print("O total a pagar é: ",vtotal)
else:
        d=(vpagar*5)/100
        vtotal=vpagar+d
        print("O total a pagar é: ",vtotal)
arq= open("compras.txt","a")
arq.write("\nO valor de sua compra foi de: "+str(vpagar))
arq.write("\nA forma de pagamento foi: "+str(opcao))
arq.write("\nO valor de sua compra foi de: ",+str(vtotal))
arq.close()
