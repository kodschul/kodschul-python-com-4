# with a list

numbers = []

total = 0

while True:
    num_text = input("Enter a num: ")
    if num_text.replace("-", "").isnumeric():
        num = int(num_text)
        total += num
        
        numbers.append(num)
        numbers_text = " + ".join([str(x) for x in numbers])
        print(f"{numbers_text} = {total}")
    elif num_text == "=":
        break
    else: 
        print(f" {num_text} is not a valid number, try again!")


print(f"Final Total = {total}") 
    
    
    
# Without a list

total = 0

while True:
    num_text = input("Enter a num: ")
    if num_text.replace("-", "").isnumeric():
        num = int(num_text)
        total += num
        print(f"Total = {total}")
    elif num_text == "=":
        break
    else: 
        print(f" {num_text} is not a valid number, try again!")


print(f"Final Total = {total}") 
    
    