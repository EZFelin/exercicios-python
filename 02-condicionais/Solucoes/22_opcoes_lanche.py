print("1. cachorro-quente")
print("2. torrada simples")
print("3. torrada com ovo")
print("4. xis salada")
print("5. pipoca")
m=int(input("Escolha uma opção de lanche do menu: "))
q=int(input("escreva a quantidade de unidades: "))
if m==1:
      print("O valor total á pagar pelo lanche: ",q*12)
if m==2:
      print("O valor total á pagar pelo lanche: ",q*8)
if m==3:
      print("O valor total á pagar pelo lanche: ",q*9.50)
if m==4:
      print("O valor total á pagar pelo lanche: ",q*18)
if m==5:
      print("O valor total á pagar pelo lanche: ",q*5) 
else:
    print("Valor Inválido")