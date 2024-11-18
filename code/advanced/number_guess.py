from random import randint


number_guess = randint(1, 10)
remaining_attempts = 3
input_number = None

print("------------------------------------------------")
print("----------- Guess Number Game ------------------")
print("----------- Guess a number between 1-10 to win!-")
print("------------------------------------------------")
print("")


def is_guess_correct(input_number, correct_number):
    return input_number == correct_number


def is_game_over(remaining_attempts):
    return remaining_attempts < 1


def show_hint(input_number, correct_number):
    if input_number > correct_number:
        print(f"Sorry, {input_number} is too high")
    else:
        print(f"Sorry, {input_number} is too low")


while input_number != number_guess and not is_game_over(remaining_attempts):
    input_number = int(input("Guess the number: "))

    if is_guess_correct(input_number, number_guess):
        break

    show_hint(input_number, number_guess)

    remaining_attempts -= 1

    if remaining_attempts > 1:
        print(f"You have {remaining_attempts} attempts left, think again!")

if is_guess_correct(input_number,  number_guess):
    print(f"Congratulations! {input_number} is the correct number!")
else:
    print(f"Unfortunately you lost! The correct number was {number_guess}")
