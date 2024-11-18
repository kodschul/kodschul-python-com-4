print("--- Taschenrechner ---")

ans = 0


def format_num(raw_num):
    num = float(raw_num.replace(",", "."))
    return num


def print_answer(answer):
    print("ANSWER: " + str(answer))


while True:
    input_text = input()

    if input_text == "+":
        num_text = input(str(ans) + " + ")
        num = format_num(num_text)
        ans = ans + num
        print_answer(ans)

    elif input_text == "-":
        num_text = input(str(ans) + " - ")
        num = format_num(num_text)
        ans = ans - num
        print_answer(ans)

    elif input_text == "*":
        num_text = input(str(ans) + " * ")
        num = format_num(num_text)
        ans = ans * num
        print_answer(ans)

    elif input_text == "c":
        ans = 0
        print("Cleared!")
        print_answer(ans)

    elif input_text == "=":
        print(ans)
        break

    else:
        ans = format_num(input_text)
