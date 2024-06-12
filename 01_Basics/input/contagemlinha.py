# Código exemplo
# Criando o arquivo com várias linhas
with open("linhas.txt", "w") as file:
    file.write("Linha 1\nLinha 2\nLinha 3\nLinha 4\nLinha 5")

# Contando o número de linhas
with open("linhas.txt", "r") as file:
    linhas = file.readlines()

print(f"O arquivo 'linhas.txt' tem {len(linhas)} linhas.")
