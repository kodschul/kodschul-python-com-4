# Integers & Floats
num1 = float(input("enter number 1 = "))
num2: float = float(input("enter number 2 = "))


def add1(num1, num2):
    return num1 + num2


def add2(num1: int, num2: int):
    return num1 + num2


def add3(num1: int, num2: int) -> int:
    return num1 + num2


addition = round(num1 + num2, 2)
subtraction = round(num2 - num1, 2)
multiplication = round(num1 * num2, 2)
division = round(num1 / num2, 2)


print(f"Addition = {num1} + {num2} = {addition}")
print(f"Subtraction = {num2} - {num1} = {subtraction}")
print(f"Division = {division}")
print(f"Multiplication = {multiplication}")
