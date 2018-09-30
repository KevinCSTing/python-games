import random
words = ["dog","cat","bird","horse","fish"]

def main(generated_word):
    #print(generated_word)
    count = 1
    print("I'm thinking of an animal. You have ", count, " chance to try.")
    guess = input("Can you guess what it is?\n")
    if(check(guess, generated_word) == False):
        print("Wrong! the word was",generated_word, ". Try again.")
    else:
        print("You guessed right!");
    '''while(count != 1 and check(guess, generated_word) == False):
        count -= 1
        print("Wrong. You have ", count, " guess/es left.")
        next_guess = input("Guess again\n")
        if(count == 1 and check(next_guess, generated_word) == False):
            print("Game over! The word was ", generated_word)
            break;
        else:
            print("You got it!")
            break;
    else:
        print("You guessed right!")'''

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
