number = input('Enter a five-digit number: ')
number = int(number)
a = (number % 10)
b = (number % 100) // 10
c = (number % 1000) // 100
d = (number % 10000) // 1000
f = (number % 100000) // 10000
print(a * 10000 + b * 1000 + c * 100 + d * 10 + f * 1)



