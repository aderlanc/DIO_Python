saldo = 500
saque = 800
cheque_especial = 200
conta_normal = False
conta_universitaria = False

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Saldo incuficiente conta normal!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente conta universitaria!")
else:
    print("Tipo de conta não informado.")