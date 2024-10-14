a = input("What is your score : ")
score = int(a)

if score >= 101:
    print("Please enter a valid score ")
    exit()

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'E'
else: grade = 'F'

print(grade)
