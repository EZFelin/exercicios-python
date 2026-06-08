# Escreva um programa que corrija uma prova de múltipla escolha com 10 questões e 5 alunos. O programa deve solicitar ao usuário que insira o gabarito da prova (as respostas corretas para cada questão) e, em seguida, solicitar as respostas de cada aluno. O programa deve comparar as respostas dos alunos com o gabarito e contar quantos acertos cada aluno teve, imprimindo o resultado para cada um. O programa deve garantir que as respostas sejam inseridas corretamente (por exemplo, apenas letras A, B, C, D ou E) e que o gabarito seja preenchido antes de tentar corrigir as provas dos alunos.
gabarito = []
print("Digite o gabarito:")

for i in range(10):
    resp = input(f"Questão {i+1}: ").upper()
    gabarito.append(resp)

for aluno in range(5):
    acertos = 0

    print("\nAluno", aluno + 1)

    for questao in range(10):
        resposta = input(f"Resposta {questao+1}: ").upper()

        if resposta == gabarito[questao]:
            acertos += 1

    print("Acertos:", acertos)