import random

def main(generatedNum):
    #print("generated number is: ", generatedNum)
    guess = int(input("Guess a number between 1-10\n"))
    if(check(guess,generatedNum) == False):
        print("Keep guessing")
        main(generatedNum)
    else:
        play_again = input("You win! Would you like to play again? y/n")
        if(play_again.lower() == "y"):
            main(random.randint(1,11))
        else:
            print("See ya!")
        

def check(guess,generatedNum):
    if(guess > generatedNum):
        print("You guessed to high!")
        return False
    elif(guess < generatedNum):
        print("You guessed to low!")
        return False
    elif(guess == generatedNum):
        print("You guessed it!")
        return True
    

if (__name__ == "__main__"):
    generatedNum = random.randint(1,11)
    main(generatedNum)
