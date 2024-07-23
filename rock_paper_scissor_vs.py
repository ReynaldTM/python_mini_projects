import random

user_wins = 0
computer_wins = 0
draws = 0

options = ["rock", "paper", "scissors"]  # list, index starts at 0

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower() # lowers all inputs
    if user_input == "q":
        break # breaks out of while loop

    if user_input not in options:  # checking if user_input is in this list
        print("Invalid input, please try again.")
        continue  # asks for input again

    random_number = random.randint(0, 2)  # randint start on 0 because of python indexing
    # rock:0, paper:1, scissors:2
    computer_pick = options[random_number] # computer picks index from options based on random number
    print("Computer picked", computer_pick + ".")  # commas add space between variables automatically

    if user_input == "rock" and computer_pick == "scissors": # logics
        print("You win!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You win!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You win!")
        user_wins += 1

    elif user_input == computer_pick:
        print("Draw, try again.!")
        draws += 1

    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("You drew with the computer", draws, "times.")
print("Goodbye!")
