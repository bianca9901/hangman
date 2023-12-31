# Hangman
## About
The Hangman Game is a classic word-guessing game that challenges players to unravel a secret word. The task is to guess the word by guessing a letter one at a time. However, be careful! If you guess an incorrect letter, you will lose a life, and a body part of the hangman figure will be drawn.

Prepare yourself to get focused. Whether you choose to play solo or in a group, the Hangman Game guarantees hours of fun while at the same time expanding your vocabulary!


The application can be accessed by this [link](https://the-hangman-game-f82c19cb0385.herokuapp.com/)

![Computer screens](documentation/images/features/computer-screen.png)

Note: This application is designed to run on pc.

---

## How to play:
1. Click [Here](https://the-hangman-game-f82c19cb0385.herokuapp.com/) to start the application.

2. You will now see a menu, with two options.

3. If you are familiar with the hangman game. Press enter to play. Otherwise, press the downward direction arrow on your keyboard, then press enter. This will take you to the instructions. Press enter again to go back to the home menu.

4. When you decide to play, you are prompted to make your first guess. Press a letter on your keyboard and then press enter.

5. When you have used all of your lives or figured out the correct word, You will be presented with a "Go back" option. Press enter and you are taken back to the home menu. Press play to start the game again and you will get a new word. Good luck and have fun!

Here is a picture so that you can get a visual understanding of the navigation throughout the application!

![app navigation](documentation/images/features/navigation.png)
---
## User Stories

### **First-Time Visitor Goals:**

* As a first-time visitor my goal is to try the Hangman Game application and understand its purpose by reading the instructions.

* As a first-time visitor my goal is to play the game so that I can understand its features.

### **Returning Visitor Goals:**

* As a returning visitor my goal is to play the game to see if my guessing skills have improved.

### **Frequent Visitor Goals:**

* As a frequent visitor my goal is to play multiple times in a row so that I can test my focus and luck.

* As a frequent visitor my goal is to play the game so that I can improve my English vocabulary.

## Existing features

### The home menu:
* Consists of two options. "Play" and "Instructions"
![Home Menu](documentation/images/features/home-page.png)

### The instructions:
* The instructions give a simple explanation of what the game is about. The player can then click on the "Go Back" button by pressing enter. This will take the player back to the home menu.
![Instructions](documentation/images/features/instructions.png)

### The Game:
1. The game begins with a welcoming message.
![Welcome message](documentation/images/features/welcome.png)
2. It then displays messages to give assurance to the player that the game has started.
![Game has started](documentation/images/features/reassuring-messages.png)
3. It then displays the text ''You have 6 lives'' which is the lives (guessing chances) the player will start with. ![You have 6 lives](documentation/images/features/six-lives.png)
4. It also displays the hangman stage, that at the moment is only a pole. 
![Hangman stage 1](documentation/images/features/hangman-pole.png)
5. Underneath the hangman stage, underscores are displayed, the number of underscores is the number of letters. Each underscore represents a hidden letter. For example, "_ _ _ _ _ _ _ _ _ " would be a word containing nine letters.                
![Underscores for secret letter](documentation/images/features/underscores.png)
6. Underneath the underscores the player is presented with an input field. "Guess a letter:" The player is prompted to type their guess.                         
![Input field](documentation/images/features/guess-a-letter.png) 
- If the guess would be anything other than a single letter, the player will get a message saying "Invalid guess! Please enter a single letter.". However, this will not affect their remaining lives, the input field will just repeat itself and the player will have to try again. ![Invalid guess](documentation/images/features/invalid-guess.png)
7. If the player guesses an incorrect letter, the first body part (the head of the hangman figure) will be drawn, and the lives will decrease to 5. 
![Incorrect guess](documentation/images/features/incorrect-letter.png)
* Important: If the same incorrect letter is guessed once again, a life will be taken once again, therefore, the player has to work on their memory skills or alternatively scroll up to see if they had already guessed that letter.
8. If the player guesses a correct letter, the underscore that contains that/or those letters will be filled in. ![Correct guess](documentation/images/features/correct-letter.png)
9. The game will continue as explained above until the player has guessed the correct word or if the player has used all of their 6 lives.
* If the player loses. They will get a message saying "YOU LOSE!" and they will, at last, know what the secret word was.      
![You lose + The correct word displayed](documentation/images/features/you-lose.png)
* If the player unravels the secret word, they will be presented with a message saying "YOU WON!".
![You won message](documentation/images/features/you-won.png)
* Either if the player wins or loses, they will see a button at the end of the screen that if pressed enter, will take them back to the home menu.           
![Go back Menu](documentation/images/features/go-back.png)
10. The player is then taken back to the home menu.

---

## Features Left to Implement

At the moment, the player has to remember previously guessed incorrect letters. Even though this could be seen as a part of the game (to remember or to scroll up to remind themselves if they had already guessed that letter), I do want to implement a logic in the future that would contribute to a better user experience.

The idea is to collect all the guessed letters and display them right next to the input field. If the player does type an already guessed letter, I will implement a message saying "You have already guessed that letter!"

---

## Data structures

Throughout the whole development, data structures were used to support the logic of the project.
* Lists were used to store and manage certain aspects of the program, such as the menu options and the words for the hangman game.
* Strings were used to handle and manipulate text within the program, such as the instructions, menu titles, and messages.

These data structures were used to achieve the functionality of the game and to provide an engaging user experience.
___

## Technologies used

### Languages:
* [Python](https://www.python.org/) was used to make the game.

### Frameworks/Libraries, Programmes, and Tools:
#### Python modules/packages:
#### Standard library imports:
* [Random](https://docs.python.org/3/library/random.html) was used to randomize the words for each round.
* [Os](https://docs.python.org/3/library/os.html) was used to clear the terminal.

#### Third-party imports:
* [Colorama](https://pypi.org/project/colorama/) was used to make the game colorful.
* [Simple term menu](https://pypi.org/project/simple-term-menu/) was used to make the menus.


#### Other tools:
* [Github](https://github.com/)
was used to host the code on the website.
* [Git](https://git-scm.com/)
was used for version control.
* [Visual studio code](https://code.visualstudio.com/)
was used to write the code.
* [MIRO](https://miro.com/) was used for the flowchart and visual representation of application navigation.
* [Heroku](https://id.heroku.com/login) was used to deploy the project.

---

## Testing
Please visit [this link](TESTING.md) to find all test-related documentation.

---
## Bugs

### Solved Bugs

Originally, it was an issue with Colorama. The selected color for the "Guess a letter:" print statement would persist and affect the letter that the player would put in. This did not look good since it was hard to tell the sections apart. Initially, I did not know where in the code I could change the color of the player input.

In the end, I could fix this issue by implementing an extra + with the color I wanted after the "Guess a letter print", like this, `Fore.BLUE + '\n\nGuess a letter: ' +
Fore.YELLOW + '\n\n'`

The bug was fixed and afterward, the player input color would be distinct from the print statement.

### Unsolved bugs
None
### Mistakes

In the initial version of my game, I had only one section for all of the code. In this section, I relied heavily on if/else/elsif statements. This quickly became messy and hard to maintain. However, after having my first project portfolio talk with my mentor, I realized the need for a better structure. Together we made a flowchart and after that, I made huge improvements by:
* Defining a lot more functions.
* Creating two sections, "Game()" and "Main()".
* In the game() section, I implemented the core of the game. Including some, but not all statements, (such as the code responsible for the hangman stages updating and input validation, etc.)
* Giving the main() section the responsibility to hold the previously mentioned newly defined functions, such as "game()" and "instructions()".

These changes made it possible to delete excessive nested if/elif/else statements. It also made the code more organized and readable by implementing two sections for the game, one whose responsibility was to hold the logic, and one whose responsibility was to hold the execution. The code is now clean and maintainable and repetition is avoided.

This mistake reminded me of the power of flowcharts. The mistake will also influence future projects positively, as I now recognize the importance of detailed planning instead of relying on an overall plan. 

--- 

## Deployment

The project was deployed to Heroku.
The project can be accessed by [this](https://the-hangman-game-f82c19cb0385.herokuapp.com/) link.

How to run this project locally:

1. This project requires Python to be installed. If you don't have Python, click [here](https://www.python.org/downloads/) to download.
2. This project contains Python packages and dependencies. Therefore, you need to install pip. You can install pip by opening your terminal and pasting this `sudo apt install python3-pip` and then pressing enter.
3. Clone this repository by copying this `git clone https://github.com/bianca9901/hangman.git` and pasting it into your terminal and then pressing enter.


How to deploy to Heroku:

1. Sign up to Heroku. Click [here](https://signup.heroku.com/login)

2. When you have registered your account, click on the "Create new app" button that is displayed on your dashboard.    
![Create new app](documentation/images/deploy-instructions/create-new-app-button.png)

3. Select a name for your app, and choose your region. Then click "Create app".
![Select name and region](documentation/images/deploy-instructions/name-region.png)

4. You are now on your newly created applications' information page. Now, click on "Settings".
![Settings](documentation/images/deploy-instructions/settings.png)
 Scroll down to Config Vars. Now click "Reveal Config Vars".
![Config vars](documentation/images/deploy-instructions/config-vars.png)
 In the field for "KEY" type PORT, in the field for "VALUE" type 8000, and then click "Add".
![Port 8000](documentation/images/deploy-instructions/port-8000.png)

5. Scroll further down and you will see "Buildpacks". Now click "Add buildpack".   
![Buildpacks](documentation/images/deploy-instructions/add-buildpacks.png)  
  In the pop up you will see a bunch of icons. You should click on the Python icon, and then click on the "Save changes" button. Then click "Add buildpacks" again, this time, click on the NODE.JS icon and the "Save changes" button afterward. Make sure Python is first in this list, and that NODE.JS is underneath (identical to the image below). The order is important.
![Correct order](documentation/images/deploy-instructions/correct-order.png)

6. Scroll back up to the navigation bar, and click on "Deploy".
![Navbar deploy](documentation/images/deploy-instructions/navbar-deploy.png)
In the "Deployment method" section, click on GitHub. Then click on "Connect to GitHub".
![Deploy](documentation/images/deploy-instructions/connect-to-github.png)

7. Search for your GitHub repository name, when this is filled in, you will be able to click "Connect".
![Repository name](documentation/images/deploy-instructions/repo-name.png)

8. Scroll down to the "Manual deploy" section and click on "Deploy Branch"
![Manual deploy](documentation/images/deploy-instructions/deploy.png)

9. After the app has been built, you will see a message "Your app was successfully deployed" Underneath this message you can click on the "View" button, this is a link that will take you to your deployed application.
![View app](documentation/images/deploy-instructions/view.png)

---

## Credits

* [Colorama](https://pypi.org/project/colorama/) was used to implement colors.
* [Simple terminal menu](https://pypi.org/project/simple-term-menu/) was used to implement the menus. 
* [Heroku](https://id.heroku.com/login) was used to deploy my project.
* [This](https://www.youtube.com/watch?v=u51Zjlnui4Y) video helped me learn how to apply colors with Colorama.
* [This](https://www.csestack.org/clear-python-interpreter-console/) article together with the inspiration from my mentor taught me how to clear terminals.
* [This](https://www.youtube.com/watch?v=Zpa-rc9e388) video together with the tips from my mentor taught me how to create menus.
* [This](https://www.youtube.com/watch?v=cJJTnI22IF8) video gave me the idea to make the hangman game.  
* [This](https://www.youtube.com/watch?v=tMJbCWHAWQ4) video was great for inspiration and planning the structure of the game. 
* [These](https://github.com/kying18/hangman/blob/master/hangman_visual.py) figures of the hangman stages inspired me to make figures for my game.
* [This](https://github.com/kying18/hangman/blob/master/words.py) is where some of the words for the game were taken from.
* [Code Institute](https://codeinstitute.net) for the deployment terminal.
* [Miro](https://miro.com/) for flowchart and visual representation of application navigation.
---

## Acknowledgments
* Thank you [Iuliia Konovalova](https://github.com/IuliiaKonovalova), for always giving me valuable feedback, tips, and guidance.
* Thank you [Code Institute](https://codeinstitute.net), for great learning material, making my first experience with a backend language fun!
---