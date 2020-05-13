def prime_number(number):
    isPrime = True
    for i in range(2, number - 1):
        if number % i == 0: 
            isPrime = False
            break
    return isPrime

myNum = int(input())
result = prime_number(myNum)
print(result)
