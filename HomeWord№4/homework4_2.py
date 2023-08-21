from homework4 import Name, Age, Metod1, Metod2


class FinalClass(Name, Age, Metod1, Metod2):
    def __init__(self, name, _age):
        Name.__init__(self, name)
        Age.__init__(self, _age)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
            self._age = age


person = FinalClass("Beka", 20)
print(person.name)
print(person.age)

