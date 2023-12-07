def sacar(valor):
    saldo = 500
    if saldo >= valor:
        print(f"Valor sacado: {float(valor)}")
        print("Gostei!")
    print("Obrigado!")

sacar(600)       

def depositar(valor):
    saldo = 500
    saldo += valor
    print(f"Saldo: {saldo}")

depositar(200)    