def contar_caractere(texto, caractere):
    quantidade = 0

    for letra in texto:
        if letra == caractere:
            quantidade += 1

    return quantidade


texto = input("Digite uma frase: ")
caractere = input("Digite um caractere: ")

resultado = contar_caractere(texto, caractere)

print("Quantidade:", resultado)