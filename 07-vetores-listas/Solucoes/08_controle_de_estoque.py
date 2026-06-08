# Escreva um programa que implemente um controle de estoque para uma loja. O programa deve permitir ao usuário realizar as seguintes operações:
# 1. Inserir um novo produto no controle de estoque (código, nome e quantidade)
# 2. Modificar a quantidade em estoque de um produto (o estoque não pode ficar negativo)
# 3. Retirar um produto do controle de estoque
# 4. Exibir o estoque dos produtos (código, nome e quantidade de cada produto)
# 5. Exibir os 3 produtos com maior estoque (em ordem decrescente de quantidade)
# 6. Sair do programa
def menu():
    print("1. Inserir um novo produto no controle de estoque")
    print("2. Modificar a quantidade em estoque de um produto (o estoque não pode ficar negativo)")
    print("3. Retirar um produto do controle de estoque")
    print("4. Exibir o estoque dos produtos (código, nome e quantidade de cada produto)")
    print("5. Exibir os 3 produtos com maior estoque (em ordem decrescente de quantidade)")
    print("6. Sair do programa")
    op=int(input("Escolha sua opção: "))
    return op
def op1(c,p,q):
    print("Inserção:")
    codigo=int(input("Código: "))
    c.append(codigo)
    nome=input("Nome: ")
    p.append(nome)
    quant=int(input("Quantidade: "))
    q.append(quant)
def op2(c,p,q):
    print("Modification: ")
    c=int(input("Insira o código do produto: "))
    if(c in cod):
        quant=int(input("Qual a nova quantidade do produto? "))
        if(quant>=0):
            quantidade.insert(cod.index(c),quant)
        else:
            print(" Valor invalido de quantidade")
    else:
        print("Valor invalido de código")


    
def op3(c,p,q):
    print("Retirada: ")
    c=int(input("Qual código do produto a ser retirado? "))
    produto.pop(cod.index(c))
    quantidade.pop(cod.index(c))
    cod.pop(cod.index(c))


    
def op4(c,p,q):
    print("Exibição: ")
    tot=len(c)
    for i in range(tot):
        print("["+str(i+1)+"]:")
        print(c[i],"!",p[i],"!",q[i])
    print()
    
def op5(c,p,q):
    print("Os 3 maiores do estoque: ")
    for i in range(len(cod)):
        for w in range(i,len(cod)-i-1):
            if(quantidade[w]<quantidade[w+1]):
                quantidade[w], quantidade[w+1] = quantidade[w+1], quantidade[w]
                produto[w], produto[w+1] = produto[w+1], produto[w]
                cod[w], cod[w+1] = cod[w+1], cod[w]
    print("Três produtos com mais estoque:\n1°-\nCódigo: ",cod[0],"\nProduto: ",produto[0],"\nQauntidade em estoque: ",quantidade[0],"\n2°-\nCódigo: ",cod[1],"\nProduto: ",produto[1],"\nQauntidade em estoque: ",quantidade[1],"\n3°-\nCódigo: ",cod[2],"\nProduto: ",produto[2],"\nQauntidade em estoque: ",quantidade[2])


c=0
i=0
w=0
aux=0
cod=[]
produto=[]
quantidade=[]
op=1
while op!=6:
    op=menu()
    if op<1 or op>6:
            print("Opção inválida!")
    if op==1:
            op1(cod,produto,quantidade)
            print("Código: ",cod)
            print("Produto: ",produto)
            print("Quantidade: ",quantidade)
    elif op==2:
            op2(cod,produto,quantidade)
    elif op==3:
            op3(cod,produto,quantidade)
    elif op==4:
            op4(cod,produto,quantidade)
    elif op==5:
            op5(cod,produto,quantidade)
