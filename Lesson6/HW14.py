# Ваша задача — написать программу, которая перемножает все цифры, введенного пользователем целого числа, пока оно не станет меньше либо равной 9.
# Число пользователь с клавиатуры вводит, и оно всегда должно быть больше нуля.
# Примеры:
# 999 -> 2 # Вот почему 999: разбиваем на цифры 9 * 9 * 9 = 729 Потом 7 * 2 * 9 = 126 , потом 1 * 2 * 6 = 12 и в результате 1 * 2 = 2
# 1000 -> 0
# 423 -> 8
# 1 -> 1

a = 'yes'
while a == 'yes' or a == 'y':
    n = int(input("Enter some number: "))
    if n != 0:
        while n > 10:
            k = 1
            for i in range(len(str(n))):
                k *= int(str(n)[i])
            n = k
        print(n)
    else:
        print("Enter not 0 number")

    a = input("Do you want to continue calculation? (Enter yes or y to continue): ")
    a = a.lower()
else:
    print("Thank you! Bye!")
