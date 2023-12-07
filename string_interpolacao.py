nome = "Aderlan"
idade = 50
profissao = "Programador"
liguagem = "Python"
saldo = 45.4735

dados = {"nome": "Aderlan", "idade": "50", "saldo": 45.6666}

print("Nome: %s, Idade: %d" %(nome, idade)) #este método está em desuso
print("Nome: {}, Idade: {}".format(nome, idade)) #pega na sequencia informada
print("Nome: {1}, Idade: {0}".format(idade, nome)) #informo o índica da sequencia, começada em 0
print("Nome: {name}, Idade: {age} {name}".format(name = nome, age = idade)) #desta forma passa usando a variável correspondente
print("Nome: {nome}, Idade: {idade}, Saldo: {saldo}".format(**dados)) #utiliza uma lista
print(f"Nome: {nome}, Idade: {idade}, Saldo: {saldo}") #método mais utilizado - usa o nome das próprias variáveis
print(f"Nome: {nome}, Idade: {idade}, Saldo: {saldo:.2f}") #formatando meu número com 2 casas decimais
print(f"Nome: {nome}, Idade: {idade}, Saldo: {saldo:10.3f}") #informando um tamanho 10 pra minha string saldo e formatando com 3 casas