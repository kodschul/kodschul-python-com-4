# class Animal:

#     def __init__(self, name, age):
#         print(f"A new animal was born, {name} ")
#         self.name = name
#         self.age = age

#     def greet(self):
#         print(f"Hi {self.name}, you're {self.age} y/o")


# print("Animal class")

# dog = Animal("dog", 5)
# cat = Animal("cat", 3)

# dog.greet()
# cat.greet()

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
