name_list = ["mike", "eva", "alicia"]
age_list = [20, 40, 35]

# i = 0 
# for name in name_list: 
#     age = 0
#     print(f"{name.capitalize()} ist {age_list[i]} Jahre alt!")
#     i += 1
    

person_items = [["mike", 20], ["eva", 40], ["alicia", 35]]
for person_item in person_items:
    print(f"{person_item[0].capitalize()} ist {person_item[1]} Jahre alt!")




person_profiles = [{'age': 20, 'name': "Mike"}, {'name': "Mike", 'age': 20}]

for profile in person_profiles:
    print(f"{profile.get('name')} ist {profile.get('age')} Jahre alt!")
