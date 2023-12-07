curso = "CuRsO dE pYtHoN"
print(curso.upper()) #Maiúsula
print(curso.lower()) #Minúscula
print(curso.title()) #Título (primeira letra maiuscula de cada palavra)

curso = "  Python 3  "
print(curso)
print(curso.strip()) #Remove espaços em branco da direita e esquerda
print(curso.lstrip()) #Remove espaços em branco da esquerda
print(curso.rstrip()) #Remove espaços em branco da direita

curso = "Python"
print(curso.center(20)) #centraliza com 20 caracteres usando espaço em branco
print(curso.center(12, "*")) #Centraliza com 12 caracteres usando o *
print("-".join(curso)) #Coloca o caractere informado entre cada letra da palavra