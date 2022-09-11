# ДЗ 11. Модифицировать калькулятор
#
# Дописать калькулятор таким образом, чтобы он работал до тех пор, пока пользователь этого хочет
#
# Т.е. нужно делать запрос у пользователя на продолжение работы калькулятора после каждого вычисления - если пользователь ввел yes ( можно просто y), то новое вычисление, в противном случае - окончание работы.

a = 'yes'
while a == 'yes' or a == 'y':
    s = input("Choose an operation (+ - * /): ")
    if s in ('+', '-', '*', '/'):
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
    if s == '+':
        print("Result = ", x + y)
    elif s == '-':
        print("Result = ", x - y)
    elif s == '*':
        print("Result = ", x * y)
    elif s == '/':
        if y != 0:
            print("Result = ", x / y)
        else:
            print("You can't divide by zero!")
    else:
        print("Wrong operation sing!")

    a = input("Do you want to continue calculation? (Enter Yes or y to continue): ")
    a = a.lower()
else:
    print("Thank you! Bye!")
