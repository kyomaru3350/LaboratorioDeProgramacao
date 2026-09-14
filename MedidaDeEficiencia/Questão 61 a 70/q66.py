def calcular_animais():
    cabecas = 35
    pernas = 94

    coelhos = (pernas - cabecas * 2) / 2
    galinhas = cabecas - coelhos

    return galinhas, coelhos


galinhas, coelhos = calcular_animais()

print("Galinhas:", int(galinhas))
print("Coelhos:", int(coelhos))