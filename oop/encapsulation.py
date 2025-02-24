class Person:
    def __init__(self, name):
        self.__name = name  # Private variable

    def get_name(self):
        return self.__name

p = Person("Alice")
print(p.get_name())