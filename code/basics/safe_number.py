num = None

while True:
    num_text = input("Enter a num: ")

    if num_text.isnumeric():
        num = float(num_text)
        break
    else:
        print(f" {num_text} is not a valid number, try again!")

print(f"{num} is a valid number!")
