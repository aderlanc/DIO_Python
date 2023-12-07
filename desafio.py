menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Informe o valor do depósito:"))
        if deposito < 1:
            print("Valor inválido!")
            continue
        else:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:10.2f} (+)\n"
    elif opcao == "s":
        if numero_saques > LIMITE_SAQUES:
            print("Limite de saque diários excedido.")
        else:
            saque = float(input("Informe o valor do saque:"))
            if saque > saldo:
                print("Saldo insuficiente.")
            elif saque > limite:
                print("Valor limite por saque excedido.")
            else:
                saldo -= saque
                extrato += f"Saque:    R$ {saque:10.2f} (-)\n"
    elif opcao == "e" :
        print("**********Extrato**********")
        print("Sem movimento." if not extrato else extrato)
        print(f"\nSaldo:    R$ {saldo:10.2f}")
        print("***************************")
    elif opcao == "q":
        break
    else:
        print("Opção Inválida!")