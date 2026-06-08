# Escreva um programa que simule a ocupação de um ônibus com 32 lugares. O programa deve permitir ao usuário reservar ou liberar um lugar específico, bem como consultar a ocupação atual do ônibus. O programa deve continuar executando até que o usuário escolha sair.
def menu ():
    print('''1.reservar lugar
    2.liberar lugar
    3.consultar ocupação
    4.sair''')
    op=int(input("Qual sua opção?"))
    return op

def reservar(lug,oni):
    oni[lug-1]= 0
    return oni

def liberar(l,oni):
    oni[lug-1]=1
    return oni
    l=int(input("Escreva o número da poltrona que deseja liberar: "))

def consultar(oni):
    for i in range (0,32,2):
        print("[",i+1,"]=",oni[i],"[",i+2,"]=",oni[i+1])
    
onibus=[]
for i in range (32):
    onibus.append(1)

op=1
while op!=4:
    op=menu()
    if op==1:
        lug=int(input("reservar qual lugar?"))
        if onibus [lug]==1:
            reservar(lug,onibus)
        else:
            print("Lugar já está ocupado")
    elif op==2:
        lug=int(input("Liberar qual lugar?"))
        if onibus[lug-1]==0:
                liberar(lug,onibus)
        else:
            print("Lugar já está ocupado")
    elif op==3:
        consultar(onibus)
