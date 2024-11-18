

def add(num, limit):

    if num > limit:
        return num

    print(num)
    return add(num + 2, limit)


add(1, 1000)
