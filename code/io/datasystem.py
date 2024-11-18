import json

print("--- Data Processing System ---")

persons = []

# -- load existing data (phase 2)

with open('persons.json', 'r') as f:
    raw_text = f.read()

# convert the raw_text into a list of persons
persons = json.loads(raw_text)

print(persons)

# -- collect new data

while True:
    name = input("Name: ")

    if name == "c":
        break

    age = input("Age: ")
    height = input("Height (in cm): ")
    weight = input("Weight (in KG): ")

    person = {
        "name": name,
        "age": int(age),
        "height": int(height),
        "weight": int(weight)
    }

    persons.append(person)

# -- processing data

persons_count = len(persons)
print(
    f"People: {persons_count} {'People' if persons_count > 1 else 'Person'}")


age_sum = 0
height_sum = 0
weight_sum = 0
for person in persons:
    age_sum = age_sum + person['age']
    height_sum = height_sum + person['height']
    weight_sum = weight_sum + person['weight']


age_average = age_sum / (persons_count if persons_count > 0 else 1)
height_average = height_sum / (persons_count if persons_count > 0 else 1)
weight_average = weight_sum / (persons_count if persons_count > 0 else 1)

print(f"Average age: {age_average}")
print(f"Average height: {height_average} cm")
print(f"Average weight: {weight_average} kg")

# -- save the existing data (phase 1)

output = json.dumps(persons)

with open('persons.json', 'w') as f:
    f.write(output)
