# Aproximação de π utilizando o método dos produtos de Wallis. O método dos produtos de Wallis é uma técnica matemática para aproximar o valor de π usando uma série infinita de produtos. A fórmula é dada por:    
# π/2 = (2/1) * (2/3) * (4/3) * (4/5) * (6/5) * (6/7) * ...
# Escreva um programa em Python que utilize o método dos produtos de Wallis para aproximar o valor de π. O programa deve solicitar ao usuário o número de termos a serem calculados na série, e então calcular e imprimir a aproximação de π com base nesse número de termos. Quanto maior o número de termos, mais precisa será a aproximação. O programa deve utilizar um loop para calcular os produtos e uma variável para armazenar o resultado final da aproximação.
def calcular_pi(termos):
    produto = 1

    numerador = 2
    denominador = 1

    for i in range(termos):
        produto = produto * (numerador / denominador)

        if i % 2 == 1:
            numerador += 2
            denominador += 2

    pi = produto * 2
    return pi


print("Pi com 10 termos:", calcular_pi(10))
print("Pi com 100 termos:", calcular_pi(100))
print("Pi com 1000 termos:", calcular_pi(1000))