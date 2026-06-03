# Faça um programa que solicite ao usuário um número inteiro para representar o número de linhas de um triângulo e um caractere para construir o triângulo. O programa deve imprimir um triângulo de caracteres com o número de linhas especificado pelo usuário. Por exemplo, se o usuário digitar 5 e o caractere "*", o programa deve imprimir:
# *
x=int(input("Digite um numero para linhas maior que 2: "))
c=str(input("Escreva um caracter: "))
y=1
while y<=x:
    print(c*y)
    y=y+1
