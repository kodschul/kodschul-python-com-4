from random import randint

correct = randint(1,10)

print("choose one from 10 , you have 3 times")

tries =3

while tries>0:

    guess= int(input("guess the number"))

    if guess == correct:

        print ("yaaaaay")

        break

    elif guess > correct:

        print("too high")

    else:

        print("too small")

        tries -=1

        if tries>0:

            print(f"you just have{tries}times")

        else:

            print(f"you lost the correct is {correct}")
