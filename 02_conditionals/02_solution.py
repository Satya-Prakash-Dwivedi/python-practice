age = input("what is your age : ")
age_number = int(age)

day = input("Is the day today wednesday :")

price = 12 if age_number > 12 else 8

if day == 'yes':
    price -= 2

print(price)