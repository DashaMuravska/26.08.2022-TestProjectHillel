x = int(input("Enter number with 4 signs: "))
one = x // 1000
two = x // 100 % 10
three = x // 10 % 10
four = x // 1 % 10
print(one)
print(two)
print(three)
print(four)