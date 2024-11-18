num = None 

while True:
    num_text = input("Enter a num: ")
    
    if num_text.replace("-", "").isnumeric():
        num = int(num_text)
        break
    else: 
        print(f" {num_text} is not a valid number, try again!")

print(f"{num} is a valid number!")    
    
    