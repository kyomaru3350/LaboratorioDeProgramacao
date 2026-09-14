def converter_temperatura(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius


temperatura = float(input("Digite a temperatura em Fahrenheit: "))

resultado = converter_temperatura(temperatura)

print("Temperatura em Celsius:", resultado)