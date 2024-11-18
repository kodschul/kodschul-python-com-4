print("--- Daten Erfassungssystem ---")

persons = []

# -- sammeln

while True:
    name = input("Name: ")

    if name == "c":
        break

    age = input("Alter: ")
    height = input("Körpergröße (in cm): ")
    weight = input("Gewicht (in KG): ")

    new_person = {
        "name": name,
        "age": int(age),
        "height": int(height),
        "weight": int(weight)
    }

    persons.append(new_person)

# -- verarbeiten

persons_count = len(persons)

print(
    f"Anzahl an Personen: {persons_count} {'Personen' if persons_count > 1 else 'Person'}")


age_sum = 0
height_sum = 0
weight_sum = 0

for person in persons:

    print(f"Hallo {person['name']}, du bist {person['age']} Jahre alt!")

    age_sum = age_sum + person['age']
    height_sum = height_sum + person['height']
    weight_sum = weight_sum + person['weight']


age_average = age_sum / (persons_count if persons_count > 0 else 1)
height_average = height_sum / (persons_count if persons_count > 0 else 1)
weight_average = weight_sum / (persons_count if persons_count > 0 else 1)

print(age_average)
print(height_average)
print(weight_average)
