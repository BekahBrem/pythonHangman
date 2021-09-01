#Hangman game
#No GUI, Just text output

import random

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
 
word = random.choice(words)

hangmanDisplay = (
"""
 ------
|     |
|
|
|
|
|
|
----------
"""
,
"""
 ------
|     |
|     O
|
|
|
|
|
----------
"""
   ,
"""
 ------
|     |
|     O
|     +
|
|
|
|
----------
"""
    ,
"""
 ------
|     |
|     O
|    -+
|
|
|
|
----------
"""
    ,
"""
 ------
|     |
|     O
|    -+-
|
|
|
|
----------
"""
    ,
"""
 ------
|     |
|     O
|   /-+-
|
|
|
|
----------
"""
    ,
"""
 ------
|     |
|     O
|   /-+-/
|
|
|
|
----------
"""
    ,
"""
 ------
|     |
|     O
|   /-+-/
|     |
|
|
|
----------
"""
    ,
"""
 ------
|     |
|     O
|   /-+-/
|     |
|     |
|
|
----------
"""
    ,
"""
 ------
|     |
|     O
|   /-+-/
|     |
|     |
|    |  
|    |   
----------
"""
    ,
"""
 ------
|     |
|     O
|   /-+-/
|     |
|     |
|    | |
|    | |
----------
"""
)

#How may hangmen we have
guessesRemaining = 10
lettersLeft = len(word)


lettersGuessed = '' #Letters guessed right
lettersGuessedWrong = ''#Letters guessed wronng to remind the player

while guessesRemaining > 0:
    
    print("\n") #Just for formatting

    #Print the hangman according to how many letters we'eve guessed wrong
    hangmanToPrint = len(lettersGuessedWrong)
    print(hangmanDisplay[hangmanToPrint])

    for letter in word:
        if letter in lettersGuessed:
            print(letter, end =" ")
        else:
            print("_", end =" ")

    print("\n")

    if len(lettersGuessedWrong) > 0:
        print("Letters guessed wrong so far: " +  lettersGuessedWrong)

    print(lettersLeft)
    
    if lettersLeft == 0:
        print("Yay, you won!! You correctly guessed the word was: " + word)
        break

    guess = input("Guess a letter: ")
    while len(guess) > 1:
        print("Please only enter 1 letter \n")
        guess = input("Guess a letter: ")

    

    if guess in lettersGuessedWrong:
        print("You guessed that already!")
    elif guess in lettersGuessed:
        print("You guessed that already!")
    else:
        if guess in word:
            print("Yay you found a letter! '" + guess + "' was correct!")
            lettersLeft -= word.count(guess)

        if guess not in word:
                guessesRemaining -= 1
                lettersGuessedWrong += guess

    lettersGuessed += guess
    
    if guessesRemaining == 0:
        print(hangmanDisplay[11])
        print("You Loose")
        break
    
