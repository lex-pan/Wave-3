import math
def hypotenuse(number, number2):
    side3 = math.sqrt(number**2 + number2**2)
    return side3
    
side1 = int(input())
side2 = int(input())
result = hypotenuse(side1, side2)

print(result)