count = 0
total_vendas = 0

while True:
    if count == 7:
        break
    count += 1
    venda_hoje = float(input("Digite o valor da venda do dia: "))
    total_vendas += venda_hoje

print(f"Valor total de vendas em 7 dias: R${total_vendas:.2f}")