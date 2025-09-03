class Animal:

    name: str
    age: int

    family = "Mammals"

    def __init__(self, name, age: int):
        print(f"A new animal was born, {name} ")
        self.name = name
        self.age = age
        self.__secret = "secret_name"
        self._protected_name = "protected_name"

    def greet(self):
        print(f"Hi {self.name}, you're {self.age} y/o")

    def show_secret(self):
        return self.__secret

    def show_protected_name(self):
        return self._protected_name


class Hund(Animal):

    def greet(self):
        super().greet()
        print("wuff")


hund = Hund("Bello", 5)

# hund._protected_name = "ABCD"
# hund.__secret = "ABC"

print(hund._Animal__secret)
# hund.greet()

exit()

# dog = Animal("dog", 5)
# dog.family = "Dog_Family"
# cat = Animal("cat", 3)

# Animal.family = "Fake"
# print("Animal class", dog.family, cat.family)


exit()
dog.greet()
cat.greet()

exit()
# # ----- car


# class Car:
#     __status = "stopped"

#     def __init__(self):
#         self.__status = "stopped"
#         self.start()

#     def start(self):
#         self.__status = "running"

#     def stop(self):
#         self.__status = "stopped"

#     def status(self):
#         return self.__status


# bmw = Car()


# print(f"The car status: {bmw.status()}")
# bmw.start()
# print(f"The car status: {bmw.status()}")

# bmw.stop()
# print(f"The car status: {bmw.status()}")

# ----- advanced car

class Car:
    status = "stopped"
    fuel = 0

    def start(self):

        if self.fuel > 0:
            self.status = "running"
            self.fuel -= 10
            self.fuel = max(0, self.fuel)
        else:
            self.status = "no_fuel"

    def tank(self, petrol):
        self.fuel += petrol

    def stop(self):
        self.status = "stopped"

    def get_status(self):
        return self.status

    def get_fuel_level(self):
        return self.fuel


benz = Car()


print(f"The car status: {benz.get_status()}, Fuel: {benz.get_fuel_level()} L")
benz.start()
print(f"The car status: {benz.get_status()}, Fuel: {benz.get_fuel_level()} L")

benz.tank(4)
print(f"The car status: {benz.get_status()}, Fuel: {benz.get_fuel_level()} L")
benz.start()
print(f"The car status: {benz.get_status()}, Fuel: {benz.get_fuel_level()} L")

benz.stop()
print(f"The car status: {benz.get_status()}, Fuel: {benz.get_fuel_level()} L")
