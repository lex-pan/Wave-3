num = int(input("a num from 1-8:"))
letter = input("Letter from a-h:")

list = { "a": 1, "b": 2, "c": 3, "d":4, "e": 5, "f": 6, "g": 7, "h": 8}
x = list[letter]

if (num + x)%2 == 0:
    print("black")
else:
    print("white")