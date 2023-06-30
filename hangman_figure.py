import colorama
from colorama import Fore

colorama.init(autoreset=True)

hangman_art = [
    Fore.CYAN + '''
       --------
       |      |
       |      O
       |     \|/
       |      |
       |     ] [
    ''' + Fore.RESET
]