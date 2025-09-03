from random import randint
random_num = randint(1, 10)

correct_number = random_num

print(f"Random Number is {random_num}")



def finde_extreme(input_list: list):
    input_list.sort()
    return input_list[-1], input_list[0]

max_wert, min_wert = finde_extreme([1, 2, 3, 4, 5])

print(f"max: {max_wert}")
print(f"min: {min_wert}")

    
