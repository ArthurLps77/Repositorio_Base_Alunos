notas = []
for i in range(4):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)

soma = sum(notas)

quantidade = 0
for _ in notas:
    quantidade += 1

media = soma / quantidade

if media >= 5:
    status = "Aprovado"
elif 3 <= media < 4:
    status = "Recuperação"
else:
    status = "Reprovado"

print(f"Notas: {notas}")
print(f"Média: {media:.2f}")
print(f"Status: {status}")