name = input("Type your name: ")
print(f"Welcome {name}, to this adventure!")

answer = input("You are an adventurer, you do quests all over the continent of your world.  \nSince work has been stable for a while "
               "and you have saved quiet a lot you decided to take time off and simple wander around.  \nYour journey took you back to your home kingdom that has remained "
               "relatively unchanged.  \nYou remember where you are, on worn dirt road surrounded by forest and mountains on the horizon.  \nIt has come to a split and you can go left or right.  Where would you like to go? ").lower()
if answer == "left":
    answer = input("You have come to a river, you can walk around or swim though it.  \nWill you walk or swim to get pass the river? ").lower()

    if answer == "swim":
        print("You tried to swim across, but the current is too strong.  You succumbed to exhuastions and drowned.  You lose.")
    elif answer == "walk":
        print("You decide to walk around the river with the current for miles.  \nAlong the way, you see nothing but lust forest, hear bird sing and wind blowing."
              "A relaxing time.  \nAfter hours of walking you make it home.  You win!")
    else:
        print("Invalid input. You lose.")

elif answer == "right":
    answer = input("You took the right path that led to the old bridge.  \nIt's made of stone and wood, thought the stones are cracked and the wood are visibly craked."
          "It looks old and wobbly.  \nDo you want to cross it or head back to split (cross/back)? ").lower()

    if answer == "cross":
        answer = input("The bridge held your weight as you careful crossed it.  You meet a stranger on the other side, do ask for directions or keep following the road before you?"
                  "(yes/no)").lower()
        if answer == "yes":
                print(" You ask to the stranger for directions to the nearest village and thank him for his time.  You walk for hours, occasionally stopping to rest and relax until you finally"
                      "make it to the village.  You win!")
        if answer == "no":
            print("You continue on your way, as you pass and meet the strangers gaze, you give an acknowleging nod and they return the same.  /nYou walk for hours feeling lost,"
                  "until you reached a the base of the mountain.  \nYou find a busy town that has been well-developed into what looks like a small fortress attched to the mountain.  "
                  "Surround by majestic stone walls with intricate carvings.  \nInside the wall, you find the town lively, streets stall selling all kind of foods and stores selling all kinds of goods."
                  "\nYou decide to look for an inn to rest and find out out where you are.  \nThere's no rush though, so you enjoy whatever the has to offer.  You WIN!")
    elif answer == "back":
        answer = input("You decide to head back to the split and take the right path.  \nYou have come to a river, you can walk around or swim though it.  \nWill you walk or swim to get pass the river? ").lower()

        if answer == "swim":
            print("You tried to swim across, but the current is too strong.  You succumbed to exhuastions and drowned.  You lose")
        elif answer == "walk":
            print("You decide to walk around the river with the current for miles.  "
                  "\nAlong the way, you see nothing but lust forest, hear bird sing and wind blowing."
              "\nA relaxing time.  After hours of walking you make it home.  You win!")
        else:
            print("Invalid input. You lose.")

    else:
        print("Invalid input. You lose.")
else:
    print("Not a valid input.")
