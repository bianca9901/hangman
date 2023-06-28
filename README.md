# Hangman

![Logo](documentation/images/logo.png)

## About
The Hangman Game is a classic word guessing game that challenges players to unravel a secret word. The task is to guess the word by guessing a letter one at a time. However, be careful! If you guess an incorrect letter, you will lose a life, and a body part of the hangman figure will be drawn.

Prepare yourself to get focused. Whether you choose to play solo or in a group, the Hangman Game guarantees hours of fun while at the same time expanding your vocabulary!


The site can be accessed by this [link](https://bianca9901.github.io/cheers-quiz/)

![Different screens](documentation/images/different-screens.png)

---

## User Stories

### **First-Time Visitor Goals:**

* As a first-time visitor my goal is to try the Hangman Game application and understand its purpose by reading the instructions.

* As a first-time visitior my goal is to play the game so that I can understand its features.

### **Returning Visitor Goals:**

* As a returning visitor my goal is to play the game to see if my guessing skills
has improved.

* As a returning visitor my goal is to play the game together with a friend so that we can play together. ?DELETE?


### **Frequent Visitor Goals:**

* As a frequent visitor my goal is try to get a winning streak of at least 5 wins
in a row so that I can test my focus and luck.

* As a frequent visitor my goal is to play the game so that I can improve my english vocabulary.

## Existing features

### The home menu:
* Consists of two options. "Play" and "Instructions"
![Home Menu](documentation/images/landingpage.png)

### The instructions:
* The instructions gives a simple explanation of what the game is about. The user can then click on the Go Back button by pressing enter. This will take the user back to the home menu.
![Instructions](documentation/images/features/)

### The Game:
1. The game begins with a welcoming message. ![Welcome message](documentation/images/features/welcome.png)
2. It then displays messages to give assurance to the user that the game has started. ![Game has started](documentation/images/features/starting-game.png)
3. It then displays the text ''You have 6 lives'' which is the default lives (guessing chances) the user will start with. ![You have 6 lives](documentation/images/features/six-lives.png)
4. It also displays the hangman figure, that at the moment is only a pole. ![Hangman stage 1](documentation/images/features/pole.png)
5. Underneath the hangman stage, underscores is displayed, the number of underscores is the number of letters. Each underscore represents a hidden letter. For example, _ _ _ _ _ would be a word containing five letters. ![Underscores for secret letter](documentation/images/features/underscores.png)
6. Underneath the underscores the user is presented with an input field. "Guess a letter:" The user is prompted to type their guess. ![Input field](documentation/images/features/guess-letter.png) 
- If the guess would be anything other than a single letter, the user will get a message saying "Invalid guess! Please enter a single letter.". However, this will not affect their remaining lives, the input field will just repeat itself and the player will have to try again. ![Invalid guess](documentation/images/features/invalid-guess.png)
7. If the user guesses an incorrect letter, the first body part (the head of the hangman figure) will be drawn, and the remaining lives will decrease to 5. ![Incorrect guess](documentation/images/features/incorrect-guess.png)
* Important: If an incorrect letter is guessed once again, a life will be taken once again, therefore the user has to work on their memory skills/or scroll up to see if they had already guessed that letter.
8. If the user guesses a correct letter, the underscore that contains that/or those letters will be filled in. ![Correct guess](documentation/images/features/correct-guess.png)
9 The game will continue as mentioned above until the user has guessed the correct word or if the user has used all of their 6 lives.
* If the user loses. They will get a message saying "YOU LOSE!" and they will, at last, know what the secret word was. ![You lose + The correct word displayed](documentation/images/features/you-lose.png)
* If the user unravels the secret word, they will be presented with a message saying "YOU WON!". ![You won message](documentation/images/features/you-win.png)

* Either if the user wins or loses, they will get a button that if pressed enter, will take them back to the home menu.![Go back menu](documentation/features/)
10. The user is then taken back to the main menu.

---

## Features left to Implement

* At the moment, the user has to remember prevouisly guessed incorrect letters. Even though this could be seen as a part of the game (to remember or to scroll up to remind themselves if they had already guessed that letter), I do want to make a collection of letters that has already been guessed in the future, displaying all of the words that has already been guessed right next to the input field.

* A favicon ??

* A custom 404 page ??

---

## Technologies used

### Languages:
* [Python](https://www.python.org/) was used to make the game.

### Frameworks/Libraries, Programmes and Tools:
#### Python modules/packages:
#### Standard library imports:
* [Random](https://docs.python.org/3/library/random.html) was used to randomize the words for each round.
* [Os](https://docs.python.org/3/library/os.html) was used to clear the terminal.

#### Third party imports:
* [Colorama](https://pypi.org/project/colorama/) was used to make the game colorful.
* [Simple term menu](https://pypi.org/project/simple-term-menu/) was used to make the menus.


#### Other tools:
* [Github](https://github.com/)
was used to host the code on the website.
* [Git](https://git-scm.com/)
was used for version control.
* [Visual studio code](https://code.visualstudio.com/)
was used to write the code.
* [FLOW](..)ASK WHAT FLOWCHART WEBSITE J USED.
* [Heroku](https://id.heroku.com/login) was used to deploy the project.

---

## Testing
Please visit [this link](TESTING.md) to find all test-related documentation.

---
## Bugs

### Solved Bugs

* Initially, it was an issue with colorama. The selected color would persist and affect all upcoming print statements. 

* I fixed it with the help of [this](https://www.youtube.com/watch?v=u51Zjlnui4Y) video. The solution was to implement a parameter called autoreset=true to the colorama module.

* The bug was fixed and afterwards I could apply colors to specific print statements without any concerns.

### Unsolved bugs
None
### Mistakes
* 

--- 

## Deployment

The site was deployed to GitHub pages.
* The steps to deploy are as follows:

* In the GitHub repository, navigate to the Settings tab
From the source section drop-down menu, select the Main Branch

* Once the main branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.

## Local deployment
How to make a local clone of this project.

1. Copy this url https://github.com/bianca9901/cheers-quiz.git
2. Open terminal.
3. Type ```git clone``` and paste the url.
4. Press enter to create your local clone.

---

## Credits

* [Colorama](https://pypi.org/project/colorama/) was used to implement colors.
* [Simple terminal menu](https://pypi.org/project/simple-term-menu/) was used to implement the menus. 
* [Heroku](https://id.heroku.com/login) was used to deploy my project.
* [This](https://www.youtube.com/watch?v=u51Zjlnui4Y) video helped me learn how to reset the previously used color to default so that I could always start with a clean slate. 
* [This](https://www.csestack.org/clear-python-interpreter-console/) article together with the inspiration from my mentor teached me how to clear terminals.
* [Simple menus in python](https://www.youtube.com/watch?v=Zpa-rc9e388) with the inspiration from my mentor and with the help of this video I learned how to create menus.
* [This](https://www.youtube.com/watch?v=cJJTnI22IF8) video gave me the idea to make the hangman game.  
* [This](https://www.youtube.com/watch?v=tMJbCWHAWQ4) video was great for inspiration and planning the structure of the game. 
* [These](https://github.com/kying18/hangman/blob/master/hangman_visual.py) figures of the hangman stages inspired me to make my own figures to implement to my game.
* [This](https://github.com/kying18/hangman/blob/master/words.py) is where the words for the game were taken from. (In my game the words with hyphen-minus were deleted).
* [This](https://www.youtube.com/watch?v=u51Zjlnui4Y) video helped me fix the colorama bug that made all the colors after the 
---

## Acknowledgments