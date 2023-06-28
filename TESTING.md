# Testing

## Validator testing

### run.py showed no errors.

![python validator](documentation/images/python-validator.png)

### hangman_stages.py
A LOT OF ERRORS? SHOULD I WRITE THEM? IT IS THE HANGMAN FIGURES SHOULD I REALLY HANDLE IT THE SAME AS RUN.PY? OR CAN I IGNORE?

### words_for_hangman.py
SAME FOR THIS ONE.

## Manual testing

| Test | Expected Result | Tested | Passed |
| --- | --- | --- | --- |
| Start the application | The application should start without any errors.  It should display the main menu | Yes | Yes |
| Select "Instructions" from the main menu | The game instructions should be displayed. | Yes | Yes |
| Select "Go back" after visiting "Instructions" | When pressed enter, the main menu should be displayed. | Yes | Yes |
| Select "Play" in the main menu | The Hangman game should start and present a welcoming message together with print statments that assures the player that the game has started. The first hangman stage, and an input field should also be displayed.| Yes | Yes |
| Guess a correct letter | If the player guesses a correct letter that is in the secret word, the letter should take the underscore/underscores place. | Yes | Yes |
| Guess an incorrect letter | If the player guesses an incorrect letter that is not in the secret word, the next hangman stage should be displayed. | Yes | Yes |
| If player makes six incorrect guesses | The last hangman stage and the correct word should be displayed. Also a "You lose" message should be shown. | Yes | Yes |
| Guess all letters correctly | If the player guesses all the letters correctly a "You won" message should be shown. | Yes | Yes |
| Select "Go back" after winning or losing | When pressed enter, the main menu should be displayed. | Yes | Yes |
___
