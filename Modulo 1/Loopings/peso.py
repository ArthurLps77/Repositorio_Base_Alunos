pesos = []

# Coleta dos pesos
for i in range(5):
    peso = float(input(f"Digite o peso da {i+1}ª pessoa (em kg): "))
    pesos.append(peso)

# Resultado
print(f"\nO maior peso lido foi: {max(pesos)} kg")
print(f"O menor peso lido foi: {min(pesos)} kg")