# Escreva um programa que simule a reserva de lugares em um teatro. O teatro tem 10 fileiras e 12 lugares em cada fileira. O programa deve permitir que o usuário reserve ou libere um lugar específico, consulte a ocupação do teatro, consulte a quantidade de lugares livres e ocupados, grave a matriz de ocupação em um arquivo de texto, e determine qual fileira tem mais ou menos ocupação. O programa deve continuar executando até que o usuário escolha a opção de sair.
def menu ():
    print('''1.reservar lugar
    2.liberar lugar
    3.consultar ocupação
    4.consultar quantidades de livres e ocupados
    5.gravar matriz
    6.qual fileira tem mais ocupação
    7-qual fileira tem menos ocupação
    8-sair''')
    op=int(input("Qual sua opção?"))
    return op
 
 
def reservar(lug,reser,tea):   
    tea[fil-1][reser-1]= 1
    return tea
 
 
def liberar(lug,reser,tea):
    tea[fil-1][reser-1]=0
    return tea
 
 
def consultar(tea):
    for i in range (0,9,2):
        print("[",i+1,"]=",tea[i],"[",i+2,"]=",tea[i+1])
 
def livres_ocupados(tea):
    livres=0
    ocupados=0
    for l in range (10):
        for c in range (12):
            if tea[l][c] == 0:
                livres += 1
            elif tea[l][c] == 1:
                ocupados += 1
    return livres, ocupados


def maislug(tea):
    mais=0
    ocupados=0
    for l in range (10):
         ocupados=0
         for c in range (12):
            if tea[l][c] == 1:
                ocupados += 1
            if ocupados>mais:
                mais=l+1
            
    return mais


def menoslug(tea):
     menos=0
     livres=0
     for l in range (10):
        livres=0
        for c in range (12):
            if tea[l][c] == 1:
                livres += 1
            if livres<=menos:
                menos=l+1
            
     return menos


def gravamatriz(teatro):
    arq= open("teatro.txt","w")
    for l in range (10):
        vet=[]
        for c in range (12):
            vet.append(0)
            arq.write(str(vet[c])+' ')
        teatro.append(vet)
        arq.write('\n')


 
teatro=[]
vet=[]
for l in range (10):
    for c in range (12):
        vet.append(0)
    teatro.append(vet)
    vet=[] 




op=1
while op!=8:
    op=menu()
    if op==1:
        fil=int(input("Escreva qual fileira deseja ocupar(1-10): "))
        reser=int(input("Escreva qual lugar da fileira deseja ocupar(1-12): "))
        if teatro [fil-1][reser-1]==0:
                reservar(fil,reser,teatro)
        else:
            print("Lugar já está ocupado")
    elif op==2:
        fil=int(input("Escreva qual fileira deseja desocupar(1-10): "))
        reser=int(input("Escreva qual lugar da fileira deseja desocupar(1-12): "))
        if teatro[fil-1][reser-1]==1:
                liberar(fil,reser,teatro)
        else:
            print("Lugar ja esta desocupado")
    elif op==3:
        consultar(teatro)
    elif op==4:
        livres, ocupados =livres_ocupados(teatro)
        print("Essa é a quantidade de bancos livres: ", livres)
        print("Essa é a quantidade de bancos ocupados: ", ocupados)
    elif op==5:
        gravamatriz(teatro)
        print("Seu arquivo foi gravado!")
    elif op==6:
        mais= maislug(teatro)
        print("Essa é a fileira com mais ocupações: ",mais)
    elif op==7:
        menos= menoslug(teatro)
        print("Essa é a fileira com mais ocupações: ",menos)




#arq= open("teatro.txt","r")
#texto = arq.readline()
#for linha in texto:
 #    lin=(int(texto))
  #   for l in range (10):
  #          vet.append(linha)
   # teatro.append(vet)
   # vet=[]
    
#arq.close()
 
#teatro=ler('teatro.txt')
