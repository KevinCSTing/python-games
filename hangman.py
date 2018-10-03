import random
words = ["dog","cat","bird","horse","fish"]

def main(generated_word):
    #print(generated_word)
    count = 3
    print("I'm thinking of an animal. You have ", count, " chances to try.")
    guess = input("Can you guess what it is?\n")
    if(check(guess, generated_word) == True):
        print("You got it on the first try!")
    else:
        print("You guessed wrong!")
        while(count>1):
            count -= 1
            print("You only have ", count, "guess/es left!")
            next_guess = input("Guess again: ")
            if(check(next_guess, generated_word) == True):
                print("You guessed it!")
                break
            elif(check(next_guess, generated_word) == False and count !=0):
                print("try again!")
        else:
            print("Game over! The word was ", generated_word)
                
            
                

def check(guess, word):
    if(guess == word):
        return True
    else:
        return False

def generateWord():
    i = random.randint(1, len(words)-1)
    return words[i]
    
if(__name__ == "__main__"):
    print("Hi there!")
    play = input("Wanna play Guess the Word? y/n \n")
    if(play == "y"):
        generated_word = generateWord()
        main(generated_word)
    else:
        print("See you next time!")
