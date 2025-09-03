from random import randint
random_num = randint(8, 15)

n = random_num
i = 0


while i <= n:
    output = ""
    
    spaces_count = n - i 
    stars_count = (i * 2) + 1
    
    output += " " * spaces_count
    output += "*" * stars_count
    
    
    print(output)
    i += 1
    

print(" "  * 3, "|||" * 4)