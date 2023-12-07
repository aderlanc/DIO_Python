MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Pode tirar CNH.")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas e práticas")
else:
    print("Não pode tirar CNH.")