while True:
    a_str = input('Введіть число 1: ')
    operator = input('Оберіть оператор +, -, *, / ')
    b_str = input('Введіть число 2: ')
    a = float(a_str)
    b = float(b_str)
    if operator == '+':
        result = a + b
    elif operator == '-':
        result = a - b
    elif operator == '*':
        result = a * b
    elif operator == '/':
        if b == 0:
            print('На 0 ділити не можна!')
            continue
        result = a / b
    else:
        print('Некоректний оператор!')
        continue
    print(f"Результат: {result}")
    continue_calculation = input('Продовжити обчислення? (y/yes): ')
    if continue_calculation.lower() not in ('y', 'yes'):
        break