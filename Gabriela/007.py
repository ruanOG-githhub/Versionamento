lista_cidades = ["Belo Horizonte"]

print(f"Lista inicial: {lista_cidades}")

for i in range(3):
    nova_cidade = input(f"Digite o nome da {i+1}ª cidade: ")
    lista_cidades.append(nova_cidade)
    print(f"Lista atualizada: {lista_cidades}")