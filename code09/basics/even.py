
# Booleans

num_text = input("Enter number: ")
try:
    num = int(num_text)
except:
    print("check input")
    exit()

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
