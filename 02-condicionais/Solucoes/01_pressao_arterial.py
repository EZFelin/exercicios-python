# Faça um programa que solicite ao usuário a pressão arterial sistólica (número superior) e diastólica (número inferior) e classifique a pressão arterial de acordo com as seguintes categorias:
# - Normal: Sistólica < 120 e Diastólica < 80
sistolica=int(input("Digite a pressão arterial sistólica(número superior): "))
diastolica=int(input("Digite a pressão arterial diastólica(número inferior): "))
if sistolica<120 and diastolica<80:
      categoria="Normal"
elif 120<=sistolica<=139 and 80<=diastolica<=89:   
     categoria="Pré-Hipertensão"
elif 140>=sistolica<=159 or 90>=diastolica<=99:   
     categoria="Pressão Arterial Elevada - Hipertensão Estágio 1"
elif sistolica>=160 or diastolica>=100:
     categoria="Pressão Arterial Elevada - Hipertensão Estágio 2"
elif sistolica>180 or diastolica>110:
      categoria="Crise Hipertensiva - Emergência Médica"
else:
    categoria="Valores desconhecidos"
print("A categoria da pressão arterial é: ", categoria)
