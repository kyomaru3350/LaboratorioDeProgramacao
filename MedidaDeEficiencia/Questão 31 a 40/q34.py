notas = {
    "João": 8.5,
    "Maria": 7.0,
    "Pedro": 9.0
}

nome = input("Digite o nome do aluno: ")

if nome in notas:
    print("Nota:", notas[nome])
else:
    print("Aluno não encontrado.")