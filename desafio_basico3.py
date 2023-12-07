# n = int(input("Informa a quantidade de testes:"))

# while(n > 0):
#      a = input("Informe a primeira string:")
#      b = input("Informe a segunda string:")
#      if b in a:
#          print("encaixa")
#      else:
#          print("nao encaixa")
#      n = n-1    


N = int(input())

while N > 0:
    entrada = input().split(" ")

    A = entrada[0]
    B = entrada[1]

    if len(B) > len(A):
        print("nao encaixa")
    elif A.endswith(B):
        print("encaixa")
    else:
        print("nao encaixa")

    N -= 1