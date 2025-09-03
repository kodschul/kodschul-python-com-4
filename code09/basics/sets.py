my_set = {1, 1, 1, 1, 2, 3}

set_a = {1, 2, 3}
set_b = {1, 2, 4, 5, 6}

set_similar = set_a.intersection(set_b)
set_diff = set_b.difference(set_a)
set_union = set_a.union(set_b)

print("intersection:", set_a, set_b, set_similar)
print("difference:", set_a, set_b, set_diff)
print("union:", set_a, set_b, set_diff)
exit()

my_set.add(1)
my_set.add(1)
my_set.add(1)
my_set.add(1)
my_set.add(4)

list_a = [1, 2, 2, 4, 5, 6, 7, 8, 2, 3]

print(list_a, len(set(list_a)))
