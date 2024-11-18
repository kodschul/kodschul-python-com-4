print("--- Taschenrechner: Addieren ---")

x = input("Zahl 1: ")
y = input("Zahl 2: ")

x = x.replace(",", ".")
y = y.replace(",", ".")

x = float(x)
y = float(y)


ans = x + y
ans = str(ans)
ans = ans.replace(".", ",")

print(ans)
