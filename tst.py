



def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")

while True:
    mode = input(
        "what d u want (VIEW existing passwords or ADD new passwords or Q to quit): "
    ).lower()

    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        pass
    else:
        print("enter a valid option.")
        continue