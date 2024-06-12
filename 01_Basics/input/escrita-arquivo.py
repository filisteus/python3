# Código exemplo
frase = input("Digite uma frase: ")

with open("frase.txt", "w") as file:
    file.write(frase)

print("A frase foi salva no arquivo 'frase.txt'")
