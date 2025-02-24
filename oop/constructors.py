class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

c = Car("Toyota", "Corolla")
print(c.brand, c.model)