# Código exemplo
itens = []
for i in range(5):
    item = input(f"Digite o item {i+1} da lista de compras: ")
    itens.append(item)

print("Sua lista de compras é:")
for item in itens:
    print(f"- {item}")
