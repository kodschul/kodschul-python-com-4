x = 5


def change_x():
    global x
    x = 10

    print(f"Local x: {x}")


print(f"Global: {x}")

change_x()

print(f"Global: {x}")
