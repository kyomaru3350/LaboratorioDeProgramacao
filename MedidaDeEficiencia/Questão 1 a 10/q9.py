livros = []
count = 0

while True:
    if count == 3:
        break
    titulo = str(input("Digite o nome do livro para registra-lo: "))
    livros.append(titulo)
    count += 1

print(livros)