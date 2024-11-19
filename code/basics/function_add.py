

# def sum_args(a=0, b=0, c=0, d=0):
#     return a + b + c + d

def sum_args(*list_of_all_args):
    return sum(list_of_all_args)

    # x  = 0
    # for num in list_of_all_args:
    #     x += num

    # return x


output = sum_args(1, 2)  # 3
print(output)
output = sum_args(1, 2, 3)  # 6
print(output)
output = sum_args(1, 2, 3, 4)  # 10
print(output)
output = sum_args(1, 2, 3, 4, 5)  # 15
print(output)
