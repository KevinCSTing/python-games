import random

def rollDice():
    return random.randint(1,7)

def main(play):
    if(play.lower() == "y"):
        print("You rolled number ",rollDice())
        play_again = input("\nwould you like to play again? y/n ")
        if(play_again.lower() == "y"):
            main(play_again)
        elif(play_again.lower() == "n"):
            print("goodbye!")
        else:
            print("Choose only y or n!")
    elif(play.lower() == "n"):
        print("okay. see ya!")

if (__name__ == "__main__"):
    play = input("Would you like to roll the dice? y/n")
    main(play)


