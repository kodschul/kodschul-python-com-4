height = 10

 

for i in range(height):

    space = ' ' * (height - i )

    stars = '*' * (2 * i + 1)

    print(space + stars)

 

# Optional: print the trunk

trunk_space = ' ' * (height - 2)

print(trunk_space + '||||||')