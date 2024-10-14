password = input("Enter your password : ")

pass_len = len(password)

if pass_len < 6:
    print("Weak")
elif pass_len < 10:
    print("Medium")
else: print("Strong")


