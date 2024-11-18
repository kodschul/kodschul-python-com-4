

x = input("x = ")
y = input("y = ")


try:
    x = int(x)
    y = int(y)

    print(x + y)
except:
    print("Sorry, du hast etwas falsches eingegeben! Bitte erneut versuchen.")


print("Programm fertig!")
