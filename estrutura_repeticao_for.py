texto = input("Digite um texto: ")
VOGAIS = "AEIOU"

#Exemplo usando um iterável

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
else:
    print("Final do laço")

#Exemplo usando o range    

for numero in range(0, 21, 2):
    print(numero, end=" ")

print("")

for numero in range(1, 11):
    print(numero, end=" ")