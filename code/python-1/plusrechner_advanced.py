print("--- Taschenrechner: Addieren ---")


def format_input(prompt):
    input_text = input(prompt)

    while input_text == "":
        print("Bitte gebe die Zahl ein!")
        input_text = input(prompt)

    # Komma formatieren
    input_text = input_text.replace(",", ".")
    num = float(input_text)
    return num


x = format_input("Zahl 1: ")
y = format_input("Zahl 2: ")

ans = x + y
ans = str(ans)
ans = ans.replace(".", ",")

print(ans)
