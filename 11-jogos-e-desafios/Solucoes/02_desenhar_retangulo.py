# Escreva um programa que leia as coordenadas de dois pontos que definem os cantos opostos de um retângulo em um plano cartesiano, e as coordenadas de um terceiro ponto. O programa deve determinar se o terceiro ponto está dentro, fora ou na borda do retângulo, e imprimir o resultado. O programa deve utilizar a estrutura de decisão if-elif-else para realizar a verificação.
x1=float(input("Escreva o ponto x1 do canto inferior esquerdo das cordenadas cartesianas"))
y1=float(input("Escreva o ponto y1 do canto inferior esquerdo das cordenadas cartesianas"))
x2=float(input("Escreva o ponto x2 do canto superior esquerdo das cordenadas cartesianas"))
y2=float(input("Escreva o ponto y2 do canto superior esquerdo das cordenadas cartesianas"))
x=float(input("Escreva o ponto x: "))
y=float(input("Escreva o ponto y: "))
if x1<x<x2 and y1<y<y2:
    print("O ponto está dentro da região retangular")
elif x==x1 or x==x2 or y==y1 or y==y2:
    print("O ponto está exatamente na borda daregião retangular")
else:
    print("O ponto está fora da região retangular")
