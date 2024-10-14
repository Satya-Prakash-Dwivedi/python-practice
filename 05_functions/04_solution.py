import math
def Multiple(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius

    return(area, circumference)

ar, cr = Multiple(4)

print("Area is : ",ar)
print("Circumference is : ",cr)