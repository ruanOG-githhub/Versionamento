nome_completo = input("Digite seu nome completo: ").strip()
parte_nome = nome_completo.split()
if len(parte_nome) > 1:
    print("Seu sobrenome é: " , parte_nome[-1])
else:
    print("Voce digitou apenas, não ha sobrenome.")