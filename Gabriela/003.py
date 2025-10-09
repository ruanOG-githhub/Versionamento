valor1 = float(input("Informe o primeiro número: "))
valor2 = float(input("Informe o segundo número: "))

if valor1 > valor2:
    resultado = "O primeiro número é maior!"
elif valor2 > valor1:
    resultado = "O segundo número é maior!"
else:
    resultado = "Os dois números são iguais!"

print(resultado)