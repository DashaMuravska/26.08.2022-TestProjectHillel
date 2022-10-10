# ДЗ 32. Корзина для покупок
#
# 1) Создайте пользовательский класс для описания товара (предположим, это задел для интернет-магазина).
# В качестве полей товара можете использовать значение цены, описание,габариты товара. Создайте пару экземпляров вашего класса и протестируйте их работу.
#
# 2) Создайте класс «Покупатель». В качестве полей можете использовать фамилию, имя, отчество, мобильный телефон и т. д.
#
# 3) Создайте класс «Заказ». Заказ может содержать несколько товаров, причем количество каждого из товаров может быть разными.
# Заказ должен быть "подвязан" к пользователю, который его осуществил. Реализуйте метод вычисления суммарной стоимости заказа.
# Определите метод str() для корректного вывода информации о этом заказе.
#User: Ivan Ivanov
# Items:
# lemon: 4 pcs.
# apple: 20 pcs.
#
#
# Код можно начать вот так:

class Item:

    def __init__(self, name, decription, demensions, price):
        self.price = price
        self.decription = decription
        self.demensions = demensions
        self.name = name

    def __str__(self):
        return f'{self.name} {self.decription} {self.demensions} {self.price}$'


class User:

    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f'User: {self.name} {self.surname}'


class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user

    def add_item(self, item, cnt):
        self.products[item] = cnt
        return cnt

    def get_item(self, item):
        return self.products.get(item)

    def get_total(self):
        total = 0
        for i, cnt in self.products.items():
            total += i.price * cnt
        return f'Total amount: {total}$\n'

    def __str__(self):
        tmp = ''
        for i, cnt in self.products.items():
            tmp += f'{str(i)}: {cnt}\n'
        return f'{self.user} \nPurchase: \n{tmp}'


user1 = User('Dasha', 'Muravska', '380666680978')
user2 = User('Jan', 'Mushinsky', '380501312008')
item1 = Item('Phone', 'Iphone 14Pro', 'Black', 1000)
item2 = Item('Phone', 'Samsung S8+', 'Black', 500)
item3 = Item('Notebook', 'Macbook Air 13', 'SpaceGrey', 2000)

purchase1 = Purchase(user1)
purchase1.add_item(item1, 1)
purchase1.add_item(item2, 2)
sum1 = purchase1.get_total()

purchase2 = Purchase(user2)
purchase2.add_item(item3, 1)
purchase2.add_item(item3, 3)
sum2 = purchase2.get_total()

print(purchase1)
print(sum1)
print(purchase2)
print(sum2)