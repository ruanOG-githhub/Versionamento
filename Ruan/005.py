familia = []

quantidade = int(input("Quantas pessoas da sua família você quer adicionar? "))

for i in range(quantidade):
    nome = input(f"Digite o nome da {i+1}ª pessoa da família: ")
    familia.append(nome)


familia.sort()

print("\nNomes da sua família em ordem alfabética:")
for nome in familia:
    print(nome)
