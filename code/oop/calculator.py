# your class comes here! ....


class Calculator:

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def divide(self, num1, num2):
        return num1 / num2

    def multiply(self, num1, num2):
        return num1 * num2


calculator = Calculator()

print(f"Addition = {calculator.add(1,2)}")
print(f"Subtraction = {calculator.subtract(3,2)}")
print(f"Division = {calculator.divide(5,2)}")
print(f"Multiplication = {calculator.multiply(5, 5)}")
