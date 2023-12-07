T = input("Digite a mensagem:")

if len(T) < 1 or len(T) > 500:
    print("Mensagem inválida!")

if len(T) >= 1 and len(T) <= 140:
    print("TWEET") 
elif len(T) > 140:
    print("MUTE")
else:
    print("Mensagem inválida")