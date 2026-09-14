notas = []

while True:
    nota = float(input("Digite a nota do aluno (digite -1 para encerrar): "))
    if nota == -1:
        break
    notas.append(nota)

print(f"A maior nota digitada foi : {max(notas)}")