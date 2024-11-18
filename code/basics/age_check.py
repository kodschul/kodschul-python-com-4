# Booleans

year_of_birth = int(input("Let me wish you HBD, When were you born? "))


age = 2024 - year_of_birth

if age >= 18: 
    print("You're free to watch!")
    
else:
    
    age_diff = 18 - age
    print(f"Come back in {age_diff} years!")