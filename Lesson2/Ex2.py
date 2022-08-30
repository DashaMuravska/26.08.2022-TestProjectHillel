x = int(input("Enter number with 5 signs (without 0): "))
one = x // 10000
two = x // 1000 % 10
three = x // 100 % 10
four = x // 10 % 10
five = x // 1 % 10
print(five * 10000 + four * 1000 + three * 100 + two * 10 + one)
