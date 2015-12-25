class Car:
    weight = 1000

    def __init__(self, weight, driver):
        self.weight = weight
        self.driver = driver

class Person:
    weight = 100

    def __init__(self, weight):
        self.weight = weight

p = Person(150)
print(Person) # class Personn back
print(p) # instance of Person Object
print("\n")
print(Car.weight)
aCar = Car(1000, p)
print (aCar)
print("\n")