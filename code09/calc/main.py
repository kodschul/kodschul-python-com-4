import calculator 
from calculator import add, subtract

def main():
    print("Welcome to my Calculator")

    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))

    addition = calculator.add(num1, num2)
    subtraction = calculator.subtract(num1, num2)

    print(f"{num1} + {num2} = {addition}")
    print(f"{num2} - {num1} = {subtraction}")


if __name__ == '__main__': 
    main()
    