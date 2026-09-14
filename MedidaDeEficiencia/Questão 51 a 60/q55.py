disciplinas = ("Matemática", "Português")

alunos = {}

for i in range(5):
    nome = input("Digite o nome do aluno: ")
    matematica = float(input("Nota de Matemática: "))
    portugues = float(input("Nota de Português: "))

    alunos[nome] = {
        "Matemática": matematica,
        "Português": portugues
    }

for nome, notas in alunos.items():
    media = (notas["Matemática"] + notas["Português"]) / 2

    print("\nAluno:", nome)
    print("Média:", media)

    if media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")

print("\nDisciplinas:")

for disciplina in disciplinas:
    print(disciplina)