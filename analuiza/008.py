frutas = ["laranja", "limão", "banana", "pera", "uva"]
for i in range(5):
    nomeFrutas  = input(f"Digite o nome da fruta {i+1}º ")
    frutas.append(nomeFrutas)  

print("\nLista final de frutas na ordem correta:")
for i, fruta in enumerate(frutas, 1):
    print(f"{i}º {fruta}")
