
def create_person(**key_value_args):
    print(key_value_args)
    
    return key_value_args


def create_person2(dict_person: dict):
    print(dict_person)
    
    return dict_person


output1 = create_person(name="abc", alter=12, beruf="abcd")
output2 = create_person(name="abc",  beruf="abcd")
output3 = create_person2({'name': 'abc', 'beruf': 'Lehrer'})

exit()
# output2 = create_person2(name="abc", alter=12, beruf="abcd")


person3 = {
    'name': "abc",
    "alter": 14,
    'beruf': "abc"
}
# output2 = create_person2(name="abc", alter=12, beruf="abcd")
