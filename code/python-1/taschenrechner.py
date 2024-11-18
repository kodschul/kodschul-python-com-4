print("--- Taschenrechner ---")

ans = 0

while True:

    input_text = input()

    if input_text == "+":
        num_text = input(str(ans) + " + ")
        num = int(num_text)
        ans = ans + num
        print("Zwischenlösung: " + str(ans))

    elif input_text == "-":
        num_text = input(str(ans) + " - ")
        num = int(num_text)
        ans = ans - num
        print("Zwischenlösung: " + str(ans))

    elif input_text == "*":
        num_text = input(str(ans) + " * ")
        num = int(num_text)
        ans = ans * num
        print("Zwischenlösung: " + str(ans))

    elif input_text == "c":
        ans = 0
        print("Cleared!")
        print("Zwischenlösung: " + str(ans))

    elif input_text == "=":
        print(ans)
        break

    else:
        ans = int(input_text)
