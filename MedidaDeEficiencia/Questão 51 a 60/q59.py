def verificar_numeros(numero1, numero2):
    if numero1 % 2 == 0 and numero2 % 2 == 0:
        return min(numero1, numero2)
    else:
        return max(numero1, numero2)


n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

resultado = verificar_numeros(n1, n2)

print("Resultado:", resultado)