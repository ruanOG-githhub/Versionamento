from datetime import datetime


ano_atual = datetime.now().year


print("=" * 50)
print("VERIFICADOR DE MAIORIDADE")
print("=" * 50)

ano_nascimento = int(input("Digite o ano em que você nasceu: "))


idade = ano_atual - ano_nascimento


print("\n" + "=" * 50)

if idade == 18:
    print(f"Você fará ou já fez 18 anos em {ano_atual}!")
    print("Bem-vindo(a) à maioridade! 🎉")
elif idade > 18:
    anos_passados = idade - 18
    print(f"Você já completou 18 anos!")
    print(f"Você tem {idade} anos em {ano_atual}.")
    print(f"Você completou 18 anos há {anos_passados} ano(s).")
else:
    anos_faltando = 18 - idade
    ano_maioridade = ano_atual + anos_faltando
    print(f"Você ainda não tem 18 anos.")
    print(f"Você tem {idade} anos em {ano_atual}.")
    print(f"Você completará 18 anos em {ano_maioridade}.")

print("=" * 50)
