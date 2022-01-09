id = str(input("What is your agent id: "))
print("Welcome to the BEN 10 quiz cadit " + id + ".")
consent = input("are u ready to answwer the questions(yes/no): ")
points = 0
import time

# sleep(2)

if consent.lower() != "yes":
    quit()
else:
    time.sleep(1)
    print("LET THE QUIZ BEGIN!" + id + ".")
    print("")
    print("")
    print("")
    print("")
    time.sleep(1)

# first question
ans = input(
    "your first question is \n Which was Ben's favorite alien as a 10 year old : "
)
if ans.lower() == "feedback":
    points += 1
    print("")
    print("that is right cadit! ")
    print("")
    print("")
    time.sleep(1)

else:
    print("")
    print("you are failing cadit.")
    print("")
    print("")
    time.sleep(1)
# second question
ans2 = input("Who created Ben 10: ")
if ans2.lower() == "Man of Action Studio":
    points += 1
    print("")
    print("that is the way cadit!")
    print("")
    print("")
    time.sleep(1)
else:
    print("")
    print("you are a idiot cadit.")
    print("")
    print("")
    time.sleep(1)
# third question.
ans3 = input("How many movie does the Ben 10 franchise have: ")

if ans3 == "4":
    points += 1
    print("")
    print("googd job cadit!")
    print("")
    print("")
    time.sleep(1)

else:
    print("")
    print("just leave cadit!")
    print("")
    print("")
    time.sleep(1)

# fourth question
ans4 = input("How many years since ben 10 first aired: ")
if ans4 == "12":
    points += 1
    print("")
    print("nice! almost there cadit.")
    print("")
    print("")
    time.sleep(1)
else:
    print("")
    print("what are 6")
    print("")
    print("")
    time.sleep(1)

# last question
ans5 = input("What's the name of his most powerful alien: ")
if ans5.lower() == "alien x":
    points += 1
    print("")
    print("Good work cadit. \nNow you will be evaluted based on your result.")
    print("")
    print("")
    print("")
    time.sleep(1)
else:
    print(
        "Dang it caddit it was the last question!!\nNow you will be evaluted based on your result."
    )
time.sleep(3)
# result

print("you scored " + str(points) + " out of 5")
print("")
print("")
print("")

print("your percentage was as follow:")
time.sleep(3)
print(str(points / 5 * 100) + "%")

if id.lower() == "satvik":
    if points > 2:
        print("congratulation! you are now a pl...")
        time.sleep(4)
        print("idiotic low intelligence species detected......wait\nPIIIINNNNAAA")
        time.sleep(1)
        print("you have been denied all plumber privileges")
        print("you will be escorted out of the system now.")
    else:
        if points < 2:
            print("YOU ARE A IDIOT CADDIT DON'T EVEN TRY AGAIN..........")
            time.sleep(4)
            print("idiotic low intelligence species detected......\nPIIIINNNNAAA")
            time.sleep(2)
            print("you have been denied all plumber privileges")
            print("you will be escorted out of the system now.")
else:
    if points > 2:
        print("congratulation! you are now a plumer.\n GOOD JOB PLUMER")
    else:
        if points < 2:
            print("YOU ARE A IDIOT CADDIT DON'T EVEN TRY AGAIN.......... OUT!!")
