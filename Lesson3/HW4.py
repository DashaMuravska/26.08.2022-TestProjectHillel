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

