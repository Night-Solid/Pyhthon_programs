# # string concatenation (aka how to put strings together)
# # suppose we want to create a string that says "subscribe to _____ "
# youtuber = "Kylie Ying" # some string variable

# # a few ways to do this
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")
# in this madlibs we will use the f-strings.
name = input("enter your name: ").capitalize()
fav_color = input("enter your color: ")
fav_sports = input("enter you favourite sports: ")
madlib = f"Hello {name}, \nI hope you are doing great! \nI also love {fav_color} \nHey and you love {fav_sports}."
print(madlib)
