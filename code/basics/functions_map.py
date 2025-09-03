
# --- dict

persons = [{"name": "Fritz", "age": 18}, {
    "name": "Paul", "age": 15},  {"name": "Marie", "age": 40}]


def sort_person_key(person):
    return person['age']


sorted_persons = sorted(persons, key=sort_person_key)

sorted_persons = sorted(persons, key=lambda person: person['age'])
print(sorted_persons)
exit()


names = map(lambda person: person.get("name"), persons)
adults = filter(lambda person: person['age'] >= 18, persons)


print(list(names))
# -----
exit()

nums = [2, 4, 6, 8, 9]

nums_squared = []
for num in nums:
    nums_squared.append(num ** 2)

print(f" {nums} ^2 = {nums_squared}")

# --- optimized
nums = [2, 4, 6, 8, 9]
nums_squared = map(lambda num: num ** 2,  nums)
print(f" {nums} ^2 = {list(nums_squared)}")


# --- option mit funktionen
nums = [2, 4, 6, 8, 9]


def square_num(num):
    return num ** 2


nums_squared = map(square_num,  nums)

print(f" {nums} ^2 = {list(nums_squared)}")
