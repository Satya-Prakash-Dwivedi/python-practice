order_size = input("Enter your order size : ")
extra_shot = input("Want an extra shot of espresso ")

if extra_shot == 'yes':
    coffee = order_size + " coffee with an extra shot of espresso"
else:
    coffee = order_size + " coffee"

print(coffee)

