from colorama import Fore


stages = [
    """
    YOU HAVE 6 LIVES

       --------
       |      |
       |
       |
       |
       |
    """,
    """
    YOU HAVE 5 LIVES LEFT

       --------
       |      |
       |      O
       |
       |
       |
    """,
    """
    YOU HAVE 4 LIVES LEFT

       --------
       |      |
       |      O
       |      |
       |
       |
    """,
    """
    YOU HAVE 3 LIVES LEFT

       --------
       |      |
       |      O
       |     \|
       |
       |
    """,
    """
    YOU HAVE 2 LIVES LEFT

       --------
       |      |
       |      O
       |     \|/
       |
       |
    """,
    """
    YOU HAVE 1 LIFE LEFT

       --------
       |      |
       |      O
       |     \|/
       |      |
       |     ]
    """,
    """
    YOU HAVE 0 LIVES LEFT

       --------
       |      |
       |      O
       |     \|/
       |      |
       |     ] [
    """
]

stages = [Fore.CYAN + stage for stage in stages]
