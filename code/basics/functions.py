

def sum_all(*args):
    total = 0
    for x in args:
        total += x
    return total


def sum_list(my_list):

    print(my_list[0])
    total = 0
    for x in my_list:
        total += x
    return total


def add(num1, num2):
    answer = num1 + num2

    print("test")
    return answer


# output = add(12, 2)
# output = sum_all(1, 2, 3)

my_list = [1, 2, 3, 4]
output = sum_list(my_list)

print(output)


# def greet(name="NoName", age=100, hobbies=None):
#     print(f"Hi {name}, {age} y/o")

#     if hobbies:
#         print("Cool, you have hobbies!")


# greet(age=20, hobbies="Coding", name="Franz")
# # greet("Franz", 20)
# greet("Mike", 21)
# greet("Michael", 40)
# greet()
