numeros = [3, 7, 10, 15, 22, 30, 42, 50]
print("Lista de números:", numeros)
numero_usuario = int(input("Digite um número para verificar se está na lista: "))
if numero_usuario in numeros:
    print(f"O número {numero_usuario} está na lista! ✅")
else:
    print(f"O número {numero_usuario} NÃO está na lista. ❌")
