
# with functions

# def greet(name="NoName", age=100, hobbies=None):
#     print(f"Hi {name}, {age} y/o")

#     if hobbies:
#         print("Cool, you have hobbies!")


# greet(age=20, hobbies="Coding", name="Franz")
# # greet("Franz", 20)
# greet("Mike", 21)
# greet("Michael", 40)
# greet()

# Without functions
# Strings, Integers & Booleans
name = input("What's your name? ")
age_str = input("How old are you? ")
is_celebrated_str = input("Did you celebrate your birthday already? (Y/N) ")

age = int(age_str)

if is_celebrated_str == "Y":
    birth_year = 2024 - age
else:
    birth_year = 2024 - age - 1


message = "Hi " + name
message += ", you are " + age_str
message += " years old and you were born in " + str(birth_year)

print(message)
