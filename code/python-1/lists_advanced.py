

numbers = []
# numbers = list()


while True:
    num_text = input("Zahl: ")

    if num_text == "c":
        break

    number = int(num_text)
    numbers.append(number)


print(numbers)
