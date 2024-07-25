import random


def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll


while True:
    players = input("Enter the number of players (2-4):  ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2-4 players.")
    else:
        print("invalid, try again.")

max_score = 50
player_scores = [0 for _ in range(players)]  # places 0 in list for number of players participating

while max(player_scores) < max_score:  # check maximum score of players to see if a player reached the limit

    for player_idx in range(players):  # will loop through list of player, simulating each player's turn
        print(f"\nPlayer, number {player_idx + 1}, turn has started!\n")  # the "+1" is because it would start at 0
        print(f"Your total score is: {player_scores[player_idx]}")
        current_score = 0

        while True:  # for player to be able to stop at any point
            should_roll = input("would you like to roll (y)? ")
            if should_roll.lower() != "y":  #
                break

            value = roll()
            if value == 1:
                print("You rolled a 1!  Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print(f"You rolled a: {value}.")

            print(f"Your score is: {current_score}")

        player_scores[player_idx] += current_score  # updating player current
        # player's score based on index position in list
        print(f"Your total score is: {player_scores[player_idx]}")

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print(f"Player number {winning_idx+1} is the winner with the score of {max_score}")