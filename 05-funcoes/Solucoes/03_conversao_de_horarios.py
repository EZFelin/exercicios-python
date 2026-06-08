# Escreva um programa que leia um horário no formato de 24 horas (HH:MM) e o converta para o formato de 12 horas (HH:MM, AM/PM). O programa deve continuar lendo horários até que o usuário digite "sair". Além disso, implemente a funcionalidade inversa, ou seja, permita que o usuário converta um horário do formato de 12 horas para o formato de 24 horas.
def converter24para12(hora, minuto):
    if hora == 0:
        return f"12:{minuto:02d}, manhã"
    elif hora < 12:
        return f"{hora}:{minuto:02d}, manhã"
    elif hora == 12:
        return f"12:{minuto:02d}, tarde"
    else:
        return f"{hora - 12}:{minuto:02d}, tarde"
def converter12para24(hora, minuto, turno):
    if turno.lower() == "manhã":
        if hora == 12:
            hora = 0
    else:  # tarde
        if hora != 12:
            hora += 12

    return f"{hora:02d}:{minuto:02d}"
opcao = 0
while opcao != 3:
    print("\n1 - Converter de 24h para 12h")
    print("2 - Converter de 12h para 24h")
    print("3 - Sair")
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        hora = int(input("Hora: "))
        minuto = int(input("Minuto: "))
        print(converter24para12(hora, minuto))
    elif opcao == 2:
        hora = int(input("Hora: "))
        minuto = int(input("Minuto: "))
        turno = input("Turno (manhã/tarde): ")

        print(converter12para24(hora, minuto, turno))

print("Programa encerrado.")