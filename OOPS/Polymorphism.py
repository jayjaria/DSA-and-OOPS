# CLASS POLYMORPHISM
# Here we have multiple classes with same method name
class Car:
    def move(self):
        print("Drive")

class Boat:
    def move(self):
        print("Sail")


class Plane:
    def move(self):
        print("Flyy")


car1 = Car()
boat1 = Boat()
plane1 = Plane()

for x in (car1, boat1, plane1):
    x.move()
