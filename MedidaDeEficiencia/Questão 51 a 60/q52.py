medicamentos = {}

for i in range(5):
    nome = input("Digite o nome do medicamento: ")
    quantidade = int(input("Digite a quantidade: "))

    medicamentos[nome] = quantidade

procurar = input("Digite o medicamento que deseja consultar: ")

if procurar in medicamentos:
    print("Quantidade em estoque:", medicamentos[procurar])
else:
    print("Medicamento não encontrado.")