a = float(input('Введіть число 1: '))
operator = input('Оберіть оператор +, -, *, / ')
b = float(input('Введіть число 2: '))
if operator == '+':
    print(a + b)
elif operator == '-':
    print(a - b)
elif operator == '*':
    print(a * b)
elif operator == '/':
    if b == 0:
        print('На 0 ділити не можна!')
    else:
        print(a / b)




