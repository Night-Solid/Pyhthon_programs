# this is a program to guess the right number in teh lesast amount of time
# hey
import random

mode = input("what do you want to play Comp/User[a] or User/Comp[b]").lower()
if mode == "a":
    num = input("please type the max number you want: ")
    if num.isdigit():
        num = int(num)
        if num <= 4:
            print("enter a number above 5")
            quit()
    else:
        print("enter a number above 5")
        quit()

    numbers = random.randint(0, num)
    guess = 0
    while True:
        guess += 1
        gess = input("please input the number: ")
        if gess.isdigit():
            gess = int(gess)

        else:
            print("enter a number!!")
            continue
        if gess == numbers:
            print("you got it. :)")
            print("you got in: ")
            print(guess)
            break
        elif gess > numbers:
            print("LESS")
        elif gess < numbers:
            print("MORE")

elif mode == "b":
    # this is a new mode that allows computer version.
    low = 1
    high = int(input("enter the max number: "))
    comp = 1
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)

        elif low == high:
            guess = low  # coz low = high
        feedback = input(f"is the {guess} high[H], low[L] or correct[C]").lower()

        if feedback == "h":
            comp += 1
            low = guess + 1
        elif feedback == "l":
            comp += 1
            high = guess - 1
    print(f"Yay! The computer guessed your number, {guess}, correctly! in {comp} tries")
else:
    print("enter a valid game mode (A/B)")
