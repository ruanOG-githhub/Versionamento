idade = int(input("Digite a sua idade: "))

if idade < 0:
    classificacao = "Idade inválida."
elif idade <= 11:
    classificacao = "Criança"
elif idade <= 18:
    classificacao = "Adolescente"
elif idade <= 24:
    classificacao = "Jovem"
elif idade <= 40:
    classificacao = "Adulto"
elif idade <= 60:
    classificacao = "Meia Idade"
else:
    classificacao = "Idoso"

print(f"Sua classificação etária é: {classificacao}") 