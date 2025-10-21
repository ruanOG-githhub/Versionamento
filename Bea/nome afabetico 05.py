familia = []
quantidade = int(input("Quantas pessoas da sua familia voce quer adicionar?:"))


for i in range(quantidade):
    nome = input(f"Digite o nome da {i+1} pessoa da familia")
    familia.append(nome)
familia.sort()

print("\nNome da sua familia em ordem alfabetica")
for nome in familia:
 print(nome)

