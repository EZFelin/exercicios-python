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


plt.barh(produto, quantidade,color="orange")
plt.xlabel('Quantidade')
plt.ylabel('Produtos')
plt.title('Gráfico de Barras')
plt.show()


