master_pwd = input(" What is the master password? ")


def view():
    with open("password.txt", "r") as f:
        for line in f.readlines():  # "readline" and "readlines" are different, apparently
            data =  line.rstrip() # "rstrip()" remove tailing space
            user, passw = data.split("|") # syntax that allows less line for making variable
            # demo
            # user,passw = [hello", "world"] # will assign input to variables based on index position
            print(f"User: {user} | Password: {passw}")

def add():
    name = input("Account  Name:")
    pwd = input("Password: ")

    with open("password.txt", "a") as f:
        f.write(name + "|" + pwd + "\n")  # will create name and password then advance to next line


# "with open"- built in python command that can read("r"), write("w"), and append("a") to files
# will automatically handle closing or any other file interacts safely
# "w" create file or overide file
# "r" read files
# "a" add something to end of a file and/or create a file if it doesn't exsist

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
