
class Car:
    __status = "stopped"
    __fuel = 0

    def start(self):

        if self.__fuel > 10:
            self.__status = "running"
            self.__fuel -= 10
            self.__fuel = max(0, self.__fuel)
        else:
            self.__status = "no_fuel"

    def tank(self, petrol):
        self.__fuel += petrol

    def stop(self):
        self.__status = "stopped"

    def get_status(self):
        return self.__status

    def get_fuel_level(self):
        return self.__fuel


benz = Car()


print(f"The car status: {benz.get_status()}, Fuel: {benz.get_fuel_level()} L")
benz.start()
print(f"The car status: {benz.get_status()}, Fuel: {benz.get_fuel_level()} L")

benz.tank(1)
print(f"The car status: {benz.get_status()}, Fuel: {benz.get_fuel_level()} L")
benz.start()
print(f"The car status: {benz.get_status()}, Fuel: {benz.get_fuel_level()} L")

benz.stop()
print(f"The car status: {benz.get_status()}, Fuel: {benz.get_fuel_level()} L")
benz.start()
print(f"The car status: {benz.get_status()}, Fuel: {benz.get_fuel_level()} L")