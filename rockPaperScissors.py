# this is a program is a python game of rock paper scissors
import random
import time

point = 0
options = ["rock", "paper", "scissors"]
print("options: rock, paper, scissors")
b = True
while True:
    first = (input("enter you thing: ")).lower()
    comp = random.choice(options)
    print("computer chose: ")
    time.sleep(0.2)
    print((comp).upper())
    if first == comp:
        print("oh! it was the same")

    elif first == "rock":
        if comp == "paper":
            print("paper wins!")
            point -= 1
        else:
            print("u won")
            point += 1

    elif first == "paper":
        if comp == "scissors":
            print("scissors wins!")
            point -= 1
        else:
            print("u won!")

            point += 1
    elif first == "scissors":
        if comp == "rock":
            print("rock wins!")

            point -= 1
        else:
            print("u won!")

            point += 1
    a = input("do you want to play again(y/n)")
    if a.lower() == "n":
        break
points = str(point)
print("YOUR SCORE WAS: " + points)
