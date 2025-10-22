cidades = []

while True:
    nome = input("Digite o nome da cidade (ou digite 'sair' para encerrar): ")
    
    if nome.lower() == 'sair':
        break  
    
    cidades.append(nome)
    print("Lista atualizada de cidades:", cidades)

print("\nLista final de cidades:")
for cidade in cidades:
    print(f"- {cidade}")
