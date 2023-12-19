import random

name = input("What is your name? ")

print("Good luck ", name,"\n")

#List of words to choose a random word from
words = ['rainbow','horse','love','crap','guess','geeks','smart','random','doctor','blanket','odd','computer']

#function to choose one random word
#for choosing random numbers it is "random.randint"
word = random.choice(words)

print("Guess the character \n")

guesses = ''

#any number of turns can be used here
turns = 12

while turns > 0:

    #count the number of times the user fails
    failed = 0
    
    for char in word:
        #comparing that character with the character in the guesses
        if char in guesses:
            print(char, end=" ") #end is to add any character at the end of the display. here, we're choosing space

        else:
            print("_")
            #this means failure, thus failure counter will be increased.
            failed = failed + 1

    if failed == 0:
        #in this case, user will win the game
        print("You win")
        print("The word is: ", word)
        break  #as the word has been found, the loop will break

    #but if the user has input the wrong alphabet, they'll have to enter another alphabet
    print()
    guess = input("guess the character")
    guesses = guesses + guess

    #checks input with the character in the word
    if guess not in word:
        turns = turns - 1

        #if the character doesn't match the word, then display
        print("wrong!")

        #counter for number of turns
        print("You have ", turns, "left to guess.")

        if turns == 0:
            print("You loose. Better luck next time. ")



