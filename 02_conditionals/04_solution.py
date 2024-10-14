fruit = input("Enter the name of fruit : ")
color = input("Enter the color of fruit : ")

if fruit == "Banana":
    if color == 'Green':
        print(fruit," is unripe")
    elif color == 'Yellow':
        print(fruit," is ripe")
    elif color == 'Brown':
        print(fruit," is overripe")
