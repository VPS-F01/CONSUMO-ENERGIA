# 1. Pede o nome do aparelho
aparelho = input("Digite o nome do aparelho (ex: Geladeira): ")

# 2. Pede a potência do aparelho em Watts (W)
potencia = float(input("Digite a potência do aparelho em Watts (W): "))

# 3. Pede o tempo médio de uso diário em horas
horas_dia = float(input("Digite o tempo médio de uso diário em horas: "))

# 4. Define o valor fixo do kWh (ex: R$ 0,50)
valor_kwh = 0.50

# 5. Calcula o consumo mensal em kWh
consumo_mensal = (potencia * horas_dia * 30) / 1000

# 6. Calcula o custo estimado em Reais (R$)
custo_estimado = consumo_mensal * valor_kwh

# 7. Mostra o resultado formatado na tela
print("-" * 35)
print(f"Aparelho: {aparelho}")
print(f"Consumo mensal: {consumo_mensal:.2f} kWh")
print(f"Custo mensal estimado: R$ {custo_estimado:.2f}")
print("-" * 35)
