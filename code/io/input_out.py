import json


first_person = None


with open('persons.json', 'r', encoding="utf-8") as f:
    persons_str = f.read()
    persons = json.loads(persons_str)
    first_person = persons[0]


with open('copy_of_persons.json', 'w+', encoding="utf8") as f:
    first_person_str = json.dumps(first_person, indent=True)
    f.write(first_person_str)
