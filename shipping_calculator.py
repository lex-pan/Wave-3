def shipping_calculator(number):
    n = 0
    if number > 1:
        n += 10.95
        number -= 1
        number *= 2.95
        n += number
        return n
numberOfItems = int(input("Insert number of items:")) 
result = shipping_calculator(numberOfItems)

print(result)
    
