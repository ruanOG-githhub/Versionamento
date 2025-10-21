#classificação idade 
idade = int(input("Digite a sua idade: "))

if idade  < 0:
    classificação = "idade invalida"
else idade <= 11: 
    classificação = "Crianca"
else idade <= 24: 
    classificação = "Adolescente"
else idade <= 40: 
    classificação = "Adulto"
else idade <= 100: 
    classificação = "idoso"
  
  print(f"Sua classificação étaria é:{classificação}")