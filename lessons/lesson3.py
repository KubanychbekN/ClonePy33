class Bank:
    def __init__(self, name, age, money, password):
        self.__name = name
        self.__age = age
        self.__money = money
        self.__passw = password

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,meaning):
        self.__name =meaning

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, meaning):
            self.__age = meaning

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, meaning):
        if meaning >= 0:
             self.__money = meaning

        else:
             print("Сумма не может быть отрицательной")

    @property
    def password(self):
        return self.__passw

    @password.setter
    def password(self, meaning):
        if len(self.__passw)>=8:
            print("Пароль должен состоять минимум из 8 символов")
        else:
            self.__passw = meaning

    def public_data(self):
        self._protected_data()

    def _protected_data(self):
        self.__private_data()

    def __private_data(self):
        print(f'Name: {self.__name}\n'
              f'Age: {self.__age}\n'
              f'Money: {self.__money}\n'
              f'Password: {self.__passw}')


account = Bank('Бека', 20, 0, 'bekad2020')
account.public_data()
#Для изменения значений атрибутов
account.name = 'Бекболот'
account.age = 151
account.money = -5
account.password = 'p5454'
print('---------------------')
#Вывод новых значений
print(account.name)
print(account.age)
print(account.money)
print(account.password)


# инкапсуляция
# 1 капсула
# 2 уровни защиты
# 3 публичный,приватный,скрытый

# class Bank:
#     def __init__(self, name, age, money, password):
#         self.__name = name
#         self.__age = age
#         self.__money = money
#         self.__passw = password
#
#     def pname(self):
#         print(f' name: {self.__name}, age: {self.__age}, money: {self.__money}')
#
#
#     def __ppas(self):
#         print(self.__passw)
#
#     def pasww(self):
#         self.__ppas()
#
# bank = Bank('Бека', 20, 10000, 'bekad2020')
#beka._money = 123456789
#print(beka._money)
#beka.pname()
#beka.__passw = '0'
#print(beka.__passw)
#beka.pasww()
#print(dir(Bank))
