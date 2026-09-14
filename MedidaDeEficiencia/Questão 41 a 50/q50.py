alunos = {}

for i in range(5):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota: "))

    alunos[nome] = nota

soma = 0

for nota in alunos.values():
    soma += nota

media = soma / 5

print("Média da turma:", media)

print("Alunos aprovados:")

for nome, nota in alunos.items():
    if nota >= 7:
        print(nome)