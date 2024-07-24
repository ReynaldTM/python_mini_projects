from cryptography.fernet import Fernet


def load_key():  # remember to define functions before using
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''  # multi line commenting- to make sure the function isn't used again, unnecessarily

#master_pwd = input(" What is the master password? ") # didn't work, don't want to do it right now
key = load_key()
fer = Fernet(key)


def view():
    with open("password.txt", "r") as f:
        for line in f.readlines():  # "readline" and "readlines" are different, apparently
            data = line.rstrip()  # "rstrip()" remove tailing space
            user, passw = data.split("|")  # syntax that allows less line for making variable
            # demo
            # user,passw = ["hello", "world"] # will assign input to variables based on index position
            print("User: ", user, "| Password:", fer.decrypt(passw.encode()).decode())


def add():
    name = input("Account  Name: ")
    pwd = input("Password: ")

    with open("password.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(
            pwd.encode()).decode() + "\n")  # will create name and password then advance to next line
        # turing into bytes then encrypt


# "with open"- built in python command that can read("r"), write("w"), and append("a") to files
# will automatically handle closing or any other file interacts safely
# "w" create file or override file
# "r" read files
# "a" add something to end of a file and/or create a file if it doesn't exist

while True:
    mode = input(" Would you like to add new password, view existing ones, or quit? (view, add)").lower()
    if mode == "q":
        print("Exiting...")
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode. ")
        continue
