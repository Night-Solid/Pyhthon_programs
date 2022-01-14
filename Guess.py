# this is a program to guess the right number in teh lesast amount of time
# hey
from cgi import print_directory
import random

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
