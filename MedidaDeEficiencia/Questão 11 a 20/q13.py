setor1 = float(input("Digite o valor gasto do setor 1: "))
setor2 = float(input("Digite o valor gasto do setor 2: "))

if setor1 > setor2:
    print("O setor 1 gastou mais que o setor 2.")
elif setor2 > setor1:
    print("O setor 2 gastou mais que o setor 1.")
else:
    print("Os setores gastaram a mesma quantia.")