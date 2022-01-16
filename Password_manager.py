from cryptography.fernet import Fernet

def load():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


#master = input("enter the encryption key: ")

key = load() #+ master.encode()
fer = Fernet(key)
# def write():
#     key = Fernet.generate_key()
#     with open("key.key","wb") as key_file:
#         key_file.write(key)


def view():
    with open("password.txt", "r") as file:
        for line in file.readlines():
            info = line.rstrip()
            user, passw = info.split("|")
            print(" username: ", user, "\n","password: ", fer.decrypt(passw.encode()).decode(),"\n")


def add():
    name = input("enter username: ")
    password = input("enter your password: ")
    with open("password.txt", "a") as file:
        file.write(name + "|" + fer.encrypt(password.encode()).decode() + "\n")
while True:
    mode = input(
        "what d u want (VIEW existing passwords or ADD new passwords or Q to quit): "
    ).lower()

    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("enter a valid option.")
        continue
