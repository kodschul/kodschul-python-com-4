
# # splitting strings
# fruit_text = "orange;lemonade;cherry"
# fruit_list = fruit_text.split(";")
# print(fruit_list)
# exit()


name = input("Enter name: ")

print(f"User input: {name}")

# replace a portion
name = name.replace("test", "")
print(f"name without test: {name}")

# remove any whitespace
name = name.strip()

# make the first letter upper
name = name.capitalize()
print(f"capitalize name: {name}")


name_substring = name[0:2]
print(f"First 2 characters are: {name_substring}")

name_substring = name[-2:]
print(f"Last 2 characters are: {name_substring}")

print(f"your has {len(name)} characters!")
print(f"Uppercase: {name.upper()}")
print(f"Lowercase: {name.lower()}")


# check if name has whitespace
if " " in name:
    print("Please remove the whitespace from your name")

# check if "a" in name
if "a" in name:
    print('Your name has an "a" ')
else:
    print("Your name doesn't have an 'a'")


# first name:   franz
# last name:   dev
