a = input("What is the distance you will travel today : ")
dist = int(a)

if dist < 3:
    transport = 'walk'
elif dist < 15:
    transport = 'Bike'
else : 
    transport = 'Car'

print(transport)