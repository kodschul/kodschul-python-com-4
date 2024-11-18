from helpers.calculator import add, subtract
from helpers.super_calculator import super_add


num1 = int(input("Enter num1 = "))
num2 = int(input("Enter num1 = "))


print(f"{num1} + {num2} = {add(num1, num2)}")
print(f"{num2} - {num1} = {subtract(num1, num2)}")
