asterisks = 1
limit = 30
spaces = 30

while asterisks < limit:
    output = ""
    for space in range(spaces):
        output += " "

    for asterisk in range(asterisks):
        output += "*"

    print(output)
    asterisks += 2
    spaces -= 1


output = ""
for space in range(22):
    output += " "

for hashtag in range(16):
    output += "#"

print(output)
