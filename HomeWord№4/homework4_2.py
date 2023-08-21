from homework4 import Name,Age, Three,Four

class Final(Name, Age, Three, Four):
    def __init__(self, name, age):
        Name.__init__(self,name)
        Age.__init__(self,age)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
            self._age = value

person = Final("Куба", 21)
