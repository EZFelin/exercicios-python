# Escreva um programa que simule um concurso de gastronomia, onde os participantes são avaliados por um júri composto por três juízes. O programa deve permitir que o usuário insira a nota de classificação do concurso, e as notas dos três juízes para cada participante. O programa deve calcular a média das notas dos juízes para cada participante, e comparar com a nota de classificação para determinar se o participante foi premiado ou não. Se a média das notas dos juízes for maior ou igual à nota de classificação, o participante é premiado, caso contrário, ele não é premiado. O programa deve permitir que o usuário insira as notas de vários participantes, e imprimir o resultado para cada um deles.
ntcla=float(input("Escreva a nota de classificação notac: "))
n1=float(input("Escreva N1: "))
n2=float(input("Escreva N2: "))
if (1>=n1 and 6<=n1)or(1>=n2 and 6<=n2) or (1>=ntcla and 6<=ntcla):
    print("Escreva novamente,os números devem ser entre 1 e 6")
elif n1>ntcla and n2>=ntcla:
    m=(n1+n2)/2
    print("Parabéns você foi premiado e sua média foi: ",m)
else:
    n3=float(input("Escreva N3: "))
    if n3>=ntcla:
        m=(n1+n2+n3)/3
        print("parabéns você foi premiado e sua média foi: ",m)
    else:
        print("Não premiado")