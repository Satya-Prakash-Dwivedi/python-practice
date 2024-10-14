pet = input("Enter the species : ")
age = int(input("Enter the age of pet : "))

if(pet == 'dog' and age < 2):
    print(pet, " will eat puppy food")
elif(pet == 'cat' and age > 5):
    print(pet, " will eat senior cat food")