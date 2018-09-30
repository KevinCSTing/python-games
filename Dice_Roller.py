import random

sides = "|       |"
one =   "|   *   |"
two =   "| *   * |"
three = "| * * * |"


def rollDice():
    return random.randint(1,6)

def drawDice(num):
    s = "\n"
    if(num == 1):
        sec = (sides,one,sides)
        print(s.join(sec))
    elif(num == 2):
        sec = (sides,two,sides)
        print(s.join(sec))
    elif(num == 3):
        sec = (sides,three,sides)
        print(s.join(sec))
    elif(num == 4):
        sec = (sides,two,two,sides)
        print(s.join(sec))
    elif(num == 5):
        sec = (sides,two,one,two,sides)
        print(s.join(sec))
    elif(num == 6):
        sec = (sides,three,three,sides)
        print(s.join(sec))

    
def main(play):
    if(play.lower() == "y"):
        '''dice = rollDice()
        drawDice(dice)'''
        print("You rolled ")
        drawDice(rollDice())
        play_again = input("\nwould you like to play again? y/n \n")
        if(play_again.lower() == "y"):
            main(play_again)
        elif(play_again.lower() == "n"):
            print("goodbye!")
        else:
            print("Choose only y or n!")
    elif(play.lower() == "n"):
        print("okay. see ya!")

if (__name__ == "__main__"):
    play = input("Would you like to roll the dice? y/n \n")
    main(play)


