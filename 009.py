nome_completo = input("Digite seu nome completo: ").strip()
partes_nome = nome_completo.split()
if len(partes_nome) > 1:
    print("Seu sobrenome é:", partes_nome[-1])
else:
    print("Você digitou apenas um nome, não há sobrenome.")


