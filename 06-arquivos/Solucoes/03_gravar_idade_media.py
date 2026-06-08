# Escreva um programa que leia o nome e a idade de 3 pessoas, calcule a média das idades e grave os dados em um arquivo de texto. O programa deve solicitar ao usuário o nome do arquivo onde os dados serão gravados.
nome = input("Digite o nome da pessoa: ")
idade = input("Digite a idade da pessoa: ")

arquivo = open("pessoas.txt", "a")

arquivo.write(nome + " " + idade + "\n")

arquivo.close()

arq= open("pessoas.txt","a")
# arq.write("A média das idades é de: " + str((int(idade1) + int(idade2) + int(idade3)) / 3))
# Aqui eu já tinha escrito a média das idades, mas como o exercício pede para ler os dados do arquivo, eu não posso usar as variáveis idade1, idade2 e idade3, então eu vou ler o arquivo e calcular a média das idades a partir dos dados lidos.
arq.close()
