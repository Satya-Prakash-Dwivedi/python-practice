age = input("How old are you? ")

age_int = int(age)

if age_int < 13:
    print("You are a child")
elif age_int < 20:
    print("You are a teenager")
elif age_int < 60:
    print("You are adult")
else : 
    print("You are a senior")