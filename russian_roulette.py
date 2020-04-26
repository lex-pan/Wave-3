import random
wheel_of_fortune = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36, 2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35, 0, 00]
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
green = [0, 00]
found = False
colour = False

rPos = random.randint(0, len(wheel_of_fortune))
x = wheel_of_fortune[rPos] 

for y in range(len(green)):
    if x == green[y]:
        colour = True
        print("Pay", x)
        break

if colour != True:
    print("The spin resulted in", x)
    print("Pay", x)

    for i in range(len(black)):
        if x == black[i]:
            found = True
            break

    if found == True:
        print("Pay Black")
    else:
        print("Pay Red")

    if x%2 == 0:
        print("Pay Even")
    else:
        print("Pay Odd")

    if x > 18:
        print("Pay 19-36")
    else:
        print("Pay 1-18")

        