
# fruit1 = "orange"
# fruit2 = "mango"
# fruit3 = "apple"

# print(fruit1)
# print(fruit2)
# print(fruit3)


# -- Liste sortieren

fruits = ["orange", "mango", "apple", "lemonade"]

# fruits_sorted = fruits.copy()
# fruits_sorted.sort()

# print(fruits_sorted)
# print(fruits)

# -- Elemente suchen

x = fruits.index("hggffgfxfgfx")
print(x)

exit()

fruits.insert(2, "v1")


# fruits.remove("mango")


# deleted_item = fruits.pop(1)

print(fruits)
# print(deleted_item)


exit()
fruits_count = len(fruits)


# -- Element in Liste prüfen
# if "banana" in fruits:
#     print("Yes")
# else:
#     print("No banana")


# --- For-loop

for fruit in fruits:
    ignore_fruits = ["orange", "lemonade", "apple"]
    if fruit in ignore_fruits:
        continue

    if fruit == "orange" or fruit == "lemonade" or fruit == "apple":
        continue

    print(fruit)


# --- While-loop
# i = 0

# while i < fruits_count:
#     fruit = fruits[i]
#     print(fruit)
#     i = i + 2

# fruit1 = fruits[0]
# print(fruit1)

# fruit2 = fruits[1]
# print(fruit2)

# fruit3 = fruits[2]
# print(fruit3)

# output = fruits[1:2]
