import os
import json
from datetime import datetime

person_str = '{"name": "Max Mustermann", "age": 20, "score": 15}'

person = dict(json.loads(person_str))
person.update(age=40)

person_str_updated = json.dumps(person)
# print(person.get("name"), person.get("age"))
print(person_str_updated)

print("-------------------------------------")

doc_list = os.listdir()

now = datetime.now()
print(now)

print(doc_list)

os.makedirs("test", exist_ok=True)
print("File exists?", os.path.exists("asdsadasasda.py"))