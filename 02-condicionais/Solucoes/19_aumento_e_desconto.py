s=float(input("valor do salário="))
print("1. Aumento")
print("2. Desconto")
e=int(input("Escolha sua opção: "))
if e==1 or e==2:
    p=int(input("a percentagem: "))
    if e==1:
        print("Esse é seu valor de aumento: ",(s*e)/100)
        print("Esse é seu valor de seu salário após a modificação do aumento: ",(s+(s*e)/100))
    if e==2:
        print("Esse é seu valor de desconto: ",(s*e)/100)
        print("Esse é o valor do seu salário apos a modificação do desconto: ",(s-(s*e)/100))
