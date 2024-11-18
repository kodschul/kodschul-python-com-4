person1 = {
    'name': 'Franz',
    'age': 21,
    'hobby': 'Programmer',
    'test': 'sadasd',
    # 'classes': {
    #     'class_1': {
    #         'course_name': 'Class 1'
    #     }
    # }
}


# print(person1['name'])
# print(person1['age'])
# print(person1['hobby'])
# print(person1['test'])

for key in person1:
    print(f"Your {key} is {person1[key]}")


exit()

person2 = {
    'name': 'Mike',
    'hobby': 'Football',
    'age': 40
}

persons = [person1, person2]

for person in persons:
    print(f"Hi {person['name']}, you are {person['age']} years old!")


# vars
person1_name = "Franz"
person1_hobby = "Programmer"
person1_age = 21

# list
person1_list = ["Franz",  21, "Programmer"]
person1_list[0] = "Mike"
