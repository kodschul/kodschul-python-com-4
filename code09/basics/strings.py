
# # splitting strings
# fruit_text = "orange;lemonade;cherry"
# fruit_list = fruit_text.split(";")
# print(fruit_list)
# exit()


# String formatting
x = 5 
y = 10 

ans = x + y  

print(str(x) +  " + " + str(y) + " = " + str(ans))
print("{0} + {1} = {2}   -> x ={0}, y = {1}, ans = {2}".format(x,y, ans))
print("{x} + {y} = {ans}".format_map({'x': x, 'y': y, 'ans': ans}))

print(f"{x} + {y} = {ans}")

exit()

name = input("Enter name: ")
print(f"User input: {name}")

# replace a portion
name = name.replace("test", "")
print(f"name without test: {name}")

# remove any whitespace
name = name.strip()
print(name, len(name))

# make the first letter upper
name = name.capitalize()
print(f"capitalize name: {name}")


name_substring = name[2:]
print(f"First 2 characters are: {name_substring}")

name_substring = name[-2:]
print(f"Last 2 characters are: {name_substring}")

print(f"your has {len(name)} characters!")
print(f"Uppercase: {name.upper()}")
print(f"Lowercase: {name.lower()}")

x: str | int | None = None
x = ""

y: int | None = None
y = 1
