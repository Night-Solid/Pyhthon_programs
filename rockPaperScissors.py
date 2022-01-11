# this is a program is a python game of rock paper scissors
import random
import time

point = 0
chace = 1

print("use the folling commands as - \n rock:R \n papper:P \n scissors:S")
options = "rock" "papper" "scissors"

play = int(input("please enter the number of rounds you want to play: "))
while chace < play:
    first = input("enter you thing: ").lower
    #    if first != "r" or "s" or "p":
    #        print("enter r, p or s.")
    #        break
    #    else:
    #        continue
    #  print("you chose: " + first)
    comp = options[random.randint(0, 3)]
    print("computer chose: ")
    time.sleep(2)
    print(comp)
    chace += 1

    if first == comp:
        print("oh! it was the same")
        chace -= 1
    elif first == "scissors" and comp == "paper":
        print("Nice!!")
        point += 1

    elif first == "paper" and comp == "rock":
        print("Nice!!")
        point += 1

    elif first == "rock" and comp == "scissors":
        print("Nice!!")
        point += 1

    elif first == "scissors" and comp == "rock":
        print("oh!!")

    elif first == "rock" and comp == "papper":
        print("oh!!")

    else:
        print("oh!!")

point = int(point)
if point == play / 2:
    print("congratulations!! u won!!")
else:
    print("sigh...try to be better plz")
