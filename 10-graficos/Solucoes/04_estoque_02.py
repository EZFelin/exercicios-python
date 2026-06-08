# Escreva um programa que leia o código, o nome e a quantidade de produtos em estoque, e permita que o usuário insira novos produtos até que ele escolha encerrar. O programa deve armazenar os dados em listas e, ao final, deve criar um gráfico de barras mostrando a quantidade de cada produto em estoque. O programa deve utilizar a biblioteca Matplotlib para criar o gráfico.
import matplotlib.pyplot as plt
def op1(c,p,q):
    print("Inserção:")
    codigo=int(input("Código: "))
    c.append(codigo)
    nome=input("Nome: ")
    p.append(nome)
    quant=int(input("Quantidade: "))
    q.append(quant)
  
cod=[]
produto=[]
quantidade=[]
op=1
print("1 para inserir, 2 para encerrar")
op=int(input("Escolha sua opção: "))
while op<2:
    if op==1:
        op1(cod,produto,quantidade)
        print("Código: ",cod)
        print("Produto: ",produto)
        print("Quantidade: ",quantidade)
    op=int(input("Escolha sua opção: "))


plt.bar(produto, quantidade,color="orange")
plt.xlabel('Produtos')
plt.ylabel('Quantidade')
plt.title('Gráfico de Barras')
plt.show()
