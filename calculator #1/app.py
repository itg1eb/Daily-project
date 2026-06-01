print('Калькулятор')
number_one = int(input("Введите 1 число: "))
operator = input("Введите оператор (+, -, *, /): ")
number_two = int(input("Введите 2 число: "))
if operator == "+":
    print(number_one+number_two)
elif operator == "-":
    print(number_one-number_two)
elif operator == "*":
    print(number_one*number_two) 
elif operator == "/":
    if number_two == 0:
        print('Ошибка братанчик')
    else:
        print(number_one/number_two)
else:
    print('Неверный оператор, бро')
