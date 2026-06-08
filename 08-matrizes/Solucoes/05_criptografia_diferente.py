# Escreva um programa que leia um texto livre do usuário e o criptografe utilizando uma matriz de 10 colunas. O programa deve preencher a matriz com os caracteres do texto, preenchendo as linhas da esquerda para a direita e de cima para baixo. Se o texto tiver menos de 10 caracteres, a matriz deve ser preenchida com espaços em branco. Em seguida, o programa deve ler a matriz na ordem das colunas, de cima para baixo e da esquerda para a direita, para gerar o texto criptografado. O programa também deve permitir que o usuário descriptografe o texto criptografado, lendo a matriz na ordem original de preenchimento para recuperar o texto original.
def criptografia():
    n=len(texto)
    lin=len(texto)//5
    if (len(texto)%5)>0:
        lin=lin+1
    v=0
    for l in range(lin):
        tex=[]
        for c in range(5):
            if v < n:
                tex.append(texto[v])
                v=v+1
            else:
                tex.append(" ")
        mat.append(tex)
    print(mat)
    textcripto=''
    for col in range(5):
        for linha in range(lin):
                textcripto=textcripto+mat[linha][col]
    print(textcripto)
    
def descriptografia():
    lin=len(texto)//5
    if (len(texto)%5)>0:
        lin=lin+1
    v=0
    textdescripto=''
    for linha in range(lin):
        for col in range(5):
            textdescripto=textdescripto+mat[linha][col]
    print(textdescripto)


texto=str(input("Escreva um texto livre: "))
tex=[]
mat=[]
criptografia()
descriptografia()
