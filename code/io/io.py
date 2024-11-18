
with open('people.txt', 'r') as f:
    # read the whole content
    content = f.read()

    # read line by line
    # lines = f.readlines()

# convert the content to lines
lines = content.split("\n")


names = []

for name in lines:
    name = name.strip()
    if name != '':
        names.append(name)
        print(f"Hi {name.capitalize()}, what's up?")


names_str = "\n".join(names)

with open('names.txt', 'w') as f:
    f.write(names_str)
