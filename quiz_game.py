print(" Welcome to my quiz!")

playing = input(" Would you like to play? (yes/no) ").lower()

if playing != "yes":
    print("Exiting game...")
    quit()

score = 0

print("Let play :)")

answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    score += 1
    print("Correct!")
else:
    print("Incorrect!")

answer = input("What does CU stand for? ")
if answer == "control unit":
    score += 1
    print("Correct!")
else:
    print("Incorrect!")

answer = input("What does ALU stand for? ")
if answer == "arithmetic logic unit":
    score += 1
    print("Correct!")
else:
    print("Incorrect!")

answer = input("What is the difference between for loops and while loops?"
               "\nA.  for loops go down lists and dictionaries a set number of times and while loops has to have conditionals broken before moving on"
               "\nB. for loops has to have conditionals fulfilled before moving on and while loops go down lists and dictionaries a set number of times"
               "\nC. IDK\n"
               ).lower()
if answer == "a":
    score += 1
    print("Correct!")
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer == "graphic processing unit":
    score += 1
    print("Correct!")
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer == "random access memory":
    score += 1
    print("Correct!")
else:
    print("Incorrect!")

print(f"You got {round((score/ 6) * 100, 2)}% correct!")
print(f"You got {score}  out of 6 question correct!")

