month = int(input("Digite um número de 1 a 12: "))

month_names = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

if month >= 1 and month <= 12:
    print(month_names[month-1])
else:
    print("Digite um número entre 1 e 12")