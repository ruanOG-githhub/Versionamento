idade = int(input("Digite sua idade: "))
if idade < 0:
    print("Idade inválida.")
elif idade <= 11:
    print("Classificação: Criança")
elif idade <= 18:
    print("Classificação: Adolescente")
elif idade <= 24:
    print("Classificação: Jovem")
elif idade <= 40:
    print("Classificação: Adulto")
elif idade <= 60:
    print("Classificação: Meia Idade")
else:
    print("Classificação: Idoso")
