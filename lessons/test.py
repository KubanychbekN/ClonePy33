class Bank:
    def __init__(self, name, age, money, password):
        self.__name = name
        self.__age = age
        self.__money = money
        self.__passw = password

    def public_data(self):
        self._protected_data()

    def _protected_data(self):
        self.__private_data()

    def __private_data(self):
        print(f'Name: {self.__name}\n'
              f'Age: {self.__age}\n'
              f'Money: {self.__money}\n'
              f'Password: {self.__passw}')


account = Bank('Бека', 20, 10000, 'bekad2020')

account.public_data()