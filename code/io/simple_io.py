import json

persons = []

persons.append({
    "name": "John",
    "age": 15,
    "height": 170,
    "weight": 65
})


persons.append({
    "name": "Peter",
    "age": 25,
    "height": 190,
    "weight": 80
})


persons.append({
    "name": "Marie",
    "age": 12,
    "height": 150,
    "weight": 50
})


output = json.dumps(persons)

with open('persons.json', 'w') as f:
    f.write(output)
