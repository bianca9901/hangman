import  random
import hangman_stages
import words_for_hangman

print("\nWelcome to Hangman!\n")
print("Guess the letter to uncover the secret word.")
print("You have a total of 6 lives.")

remaining_lives=6 #The number of total lives
secret_word = random.choice(words_for_hangman.words) #Selects a random word from the list
print(secret_word) #THIS WILL GET DELETED, FOR TESTING ONLY (shows the correct answer in terminal)
display=[] #The list that stores the words that displays
for i in range(len(secret_word)):
    display += '_' #Adds underscore for each letter in the secret word
print(display) #Prints the secret word with underscores
game_over=False #Game over variable starts as false
while not game_over: #Starts the game loop
    player_guess=input("\nGuess a letter:\n").lower() #Input field for player to guess a letter. Converts it to lowecase.
    for position in range(len(secret_word)): #Iterates over each position in the secret word.
        letter = secret_word[position] #Get the letter at the current position.
        if letter==player_guess: #If the guessed letter matches the letter in the current position.
            display[position]= player_guess #Update the display with the guessed letter.
    print(display) #Prints the updated display.
    if player_guess not in secret_word: #If the players guess is incorrect.
        remaining_lives -= 1 #One life less.
        if remaining_lives == 0: #If there are no remaining lives left
            game_over = True #Game over
            print("\nYOU LOOSE!\n") #Message to the player
    if '_' not in display: #If there are no underscores remaining in display
        game_over=True #Game over
        print("\nYOU WON!\n") #Message to the player
    print(hangman_stages.stages[remaining_lives]) #Prints the hangman stage based on lives left.


"""
Possible feautures to add: 

-- Show how many lives left with numbers as well, to complement the hangman figure. --
*(Added numbers to hangman file, but there should be other solution so that I 
can show more skills)

-- Inform the player if the letter selected has already been guessed in the round. --

-- Add message to player if they'd write something other than a letter. ---

-- Do you want to play again? press enter (or something). --

--- Add words ---

"""
