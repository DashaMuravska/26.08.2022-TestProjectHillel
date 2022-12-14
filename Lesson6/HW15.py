# Ваша задача — написать программу, которая переводит число во время в читабельном виде.
#
# Пользователь должен ввести число больше 0 и меньше 8639999.
#
#
#
# Число необходимо перевести в день, часы, минуты и секунды.
#
# Ну и дополнительной задачей является — забота о выводе.
#
# Слово "день" подбирается на основе кол-ва дней, а часы, минуты и секунды должны заполняться нулями при одноцифровых значениях.
#
#
#
# Пример:
#
#
#
# 0 -> 0 дней, 00:00:00
# 224930 -> 2 дня, 14:28:50
# 466289 -> 5 дней, 09:31:29
# 8639999 -> 99 дней, 23:59:59
# 22493 -> 0 дней, 06:14:53
# 7948799 -> 91 день, 23:59:59
# Подсказка: в одной минуте 60 сек. , в одном часе 60*60 сек, в одних сутках 24*60*60 сек. Т.е. используя функцию divmod или методы деления // и % вам необходимо найти соотвествующее кол-во дней, часов, минут, а то что останется - это секунды, которые меньше 60 ;)
#
# Дополнить ведущими нулями можно с помощью метода zfill(2)

# n = int(224930)
# n = int(466289)
# n = int(8639999)
# n = int(22493)
# n = int(7948799)

n = int(input("Введите число от 0 до 8639999: "))
while n < 0 or n > 8639999:
    n = int(input("Неверное число! Попробуйте еще раз!: "))
else:
    days = int(n/(60*60*24))
    hours = int(n/(60*60) - (days*24))
    minutes = int((n/60) - (days*24+hours)*60)
    seconds = int(n - ((days*60*60*24) + (hours*60*60) + (minutes*60)))

    if n == 0 or n <= 8639999:
        hours = str(hours)
        if len(hours) == 1:
            hours = hours.zfill(2)

        minutes = str(minutes)
        if len(minutes) == 1:
            minutes = minutes.zfill(2)

        seconds = str(seconds)
        if len(seconds) == 1:
            seconds = seconds.zfill(2)

        lst = [5, 6, 7, 8, 9]
        if days == 0 or str(days)[-1] in lst:
            print(n, "->", days, "дней", hours + ":" + minutes + ":" + seconds)
        elif days == 1 or str(days)[-1] == '1':
            print(n, "->", days, "день", hours + ":" + minutes + ":" + seconds)
        else:
            print(n, "->", days, "дня", hours + ":" + minutes + ":" + seconds)


