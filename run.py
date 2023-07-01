import os
import random
from colorama import Fore, Back
from simple_term_menu import TerminalMenu
import hangman_stages
import words_for_hangman
import hangman_figure


def go_back_to_menu():
    """Displays go-back option at the end of the game"""
    options = ['Go back']
    menu = TerminalMenu(options, title='Menu')
    selected_option_index = menu.show()

    if selected_option_index == 0:
        clear_screen()
        main()


def instructions():
    """Displays game instructions"""
    print(Back.BLUE + 'Instructions')
    print(Fore.BLUE + 'Guess the letter to uncover the secret word.')
    print(Fore.BLUE + 'You have a total of 6 lives.')
    go_back_to_menu()


def start_game_messages():
    """Displays that the game is starting"""
    print(Back.CYAN + '\nWelcome to Hangman! :-)\n')
    print('Starting game...')
    print('\nSuccessfully started!\n')
    print(Fore.LIGHTYELLOW_EX)


def clear_screen():
    """Clears the terminal screen"""
    _ = os.system('cls' if os.name == 'nt' else 'clear')


def display_word(word):
    """Prints the current state of the word"""
    print(' '.join(word))


def check_guess(secret_word, display, player_guess):
    """Checks if the guessed letter is correct and updates the display"""
    correct_guess = False
    for position in range(len(secret_word)):
        letter = secret_word[position]
        if letter == player_guess:
            display[position] = player_guess
            correct_guess = True
    return correct_guess


def print_hangman_stage(stage):
    """Prints the hangman stages"""
    print(hangman_stages.stages[stage])


def game():
    """Hangman game logic"""
    remaining_lives = 6
    print_hangman_stage(0)

    secret_word = random.choice(words_for_hangman.words)

    display = ['_'] * len(secret_word)

    game_over = False

    while not game_over:
        display_word(display)
        player_guess = input(
          Fore.BLUE + '\n\nGuess a letter: ' +
          Fore.YELLOW + '\n\n').lower()
        print(Fore.WHITE)

        # Input validation
        if len(player_guess) != 1 or not player_guess.isalpha():
            print(
                Fore.RED + '\nInvalid guess! Please enter a single letter.\n')
            continue

        correct_guess = check_guess(secret_word, display, player_guess)

        if not correct_guess:
            remaining_lives -= 1
            if remaining_lives == 0:
                print_hangman_stage(6)
                print(Fore.RED + '\nYOU LOSE! ( ɵ̥̥︹ɵ̥̥)\n')
                print('The correct word was: ' + secret_word + '\n')
                go_back_to_menu()
            else:
                print_hangman_stage(6 - remaining_lives)

        if '_' not in display:
            print(Fore.GREEN + '\nYOU WON! ٩( ^ᴗ^ )۶\n')
            go_back_to_menu()


def main():
    """Execution of game"""
    clear_screen()
    while True:
        print(Back.BLUE + '\n...T_H_E   H_A_N_G_M_A_N   G_A_M_E...')
        print(hangman_figure.hangman_art[0])
        options = ['Play', 'Instructions']
        menu = TerminalMenu(options, title='\n\n\nMenu ☜(⌒▽⌒)☞\n')
        selected_option_index = menu.show()

        if selected_option_index == 0:
            clear_screen()
            start_game_messages()
            game()
        elif selected_option_index == 1:
            clear_screen()
            instructions()
            input('Press Enter to go back to the menu...\n')
            clear_screen()


main()
