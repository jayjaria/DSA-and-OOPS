from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, model, company):
        self.model = model
        self.company = company

    def start(self):
        print(f"{self.company} {self.model} is starting....")

    def stop(self):
        print(f"{self.company} {self.model} is stopping....")

    @abstractmethod
    def details(self):
        pass

class Car(Vehicle):
    def __init__(self, model, company, price):
        super().__init__(model, company)
        self.price = price

    def details(self):
        print(f"{self.company} {self.model} {self.price}")


class Bike(Vehicle):
    def __init__(self, model, company, price):
        super().__init__(model, company)
        self.price = price

    def details(self):
        print(f"{self.company} {self.price}")

car = Car("A-1", "Benz", "1000")
bike = Bike("B-1", "Duke", "10000")

car.details()
car.stop()
bike.details()
bike.start()
