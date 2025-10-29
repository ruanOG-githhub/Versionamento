nome_completo = input("Digite seu nome completo: ")

partes = nome_completo.strip().split()

if len(partes) >= 2:
    sobrenome = partes[-1] 
    print("Sobrenome:", sobrenome)
else:
    print("Você digitou apenas um nome. Tente novamente com nome e sobrenome.")