from product import product

class SavdoAvtomati:
    def __init__(self, id, address, cash_balance=0):
        self.id = id
        self.address = address
        self.product = product
        self.cash_balance = cash_balance

    def add_product(self, name, price):
        self.product[name] = price

    def get_products(self):
        data = ''
        for k, v in self.product.items():
            data += f'Mahsulot nomi: {k}, Mahsulot narxi: {v}\n'
        return data

    def get_cash_balance(self):
        data = f'Balansingiz: {self.cash_balance}'
        return data

    def set_cash_balance(self, balance):
        self.cash_balance = balance


class Haridor:
    def __init__(self, card_number, card_balance, card_password, cash_balance):
        self.card_number = card_number
        self.card_balance = card_balance
        self.card_password = card_password
        self.cash_balance = cash_balance

    def get_card_balance(self):
        data = f'Kartangizdigi Balansingiz: {self.card_balance}'
        return data

    def haridor_get_cash_balance(self):
        data = f'Balansingiz: {self.cash_balance}'
        return data

    def haridor_set_cash_balance(self, balance):
        self.cash_balance = balance

    def set_card_balance(self, balance):
        self.card_balance = balance

    def get_password(self):
        data = f'Karta Paroli: {self.card_password}'
        return data

object1 = SavdoAvtomati(123123, 'waduawdadi')
object1.add_product('olma', 5000)
object1.set_cash_balance(1000)
print(object1.get_cash_balance())
print(object1.get_products())

object2 = Haridor(123123, 15000, 21445, 8732)
object2.haridor_set_cash_balance(7777)
print(object2.set_card_balance(16000))
print(object2.get_password())
print(object2.haridor_get_cash_balance())
print(object2.get_card_balance())

# 8-dars
l = [5, 9, 9]
for i in l:
    if l.count(i) == 1:
        print(i)
        break