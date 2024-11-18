
# # importiert nur eine Funktion/Variable
# from utils.rechner import add

# importiert alles
import utils.rechner as rechner

# import utils.rechner_output

x = input("X = ")
x = int(x)
y = input("Y = ")
y = int(y)
print("--------------------------")

xy_sum = rechner.add(x, y)
print(f"Summe = {xy_sum}")


xy_diff = rechner.subtract(x, y)
print(f"Differenz = {xy_diff}")


xy_product = rechner.multiply(x, y)
print(f"Produkt = {xy_product}")

xy_div = rechner.divide(x, y)
print(f"Division = {xy_div}")
