# Faça um programa que solicite ao usuário o peso (em kg) e a altura (em metros) de uma pessoa, calcule o Índice de Massa Corporal (IMC) e classifique o resultado de acordo com as seguintes categorias:
# - Muito abaixo do peso: IMC < 17.0
# - Abaixo do peso: 17.0 <= IMC < 18.5
# - Peso normal: 18.5 <= IMC < 25.0
# - Acima do peso: 25.0 <= IMC < 30.0
# - Obesidade grau 1: 30.0 <= IMC < 35
# - Obesidade grau 2: 35.0 <= IMC <= 40.0
# - Obesidade grau 3: IMC > 40.0
peso=float(input("Me informe seu peso: "))
altura=float(input("Me informe sua altura: "))
imc=(peso/(altura*altura))
if imc<=16.9:
    print(f"Muito abaixo do peso,esse é seu imc {imc:,.1f}km/m²")
elif imc>=17 and imc<=18.4:
    print(f"Abaixo do peso,esse é seu imc {imc:,.1f}km/m²")
elif imc>=18.5 and imc<=24.9:
    print(f"Peso normal,esse é seu imc {imc:,.1f}km/m²")
elif imc>=25 and imc<=29.9:
    print(f"Acima do peso,esse é seu imc {imc:,.1f}km/m²")
elif imc>=30 and imc<=34.9:
    print(f"Obesidade grau 1,esse é seu imc {imc:,.1f}km/m²")
elif imc>=35 and imc<=40:
    print(f"Obesidade grau 2,esse é seu imc {imc:,.1f}km/m²")
elif imc>40:
    print(f"Obesidade grau 3,esse é seu imc {imc:,.1f}km/m²")
