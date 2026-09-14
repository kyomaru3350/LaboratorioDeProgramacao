try:
    arquivo = open("relatorio_vendas.txt", "r")

    texto = arquivo.read()

    print(texto)

except FileNotFoundError:
    print("O arquivo não foi encontrado.")

finally:
    print("Encerrando o acesso ao arquivo.")