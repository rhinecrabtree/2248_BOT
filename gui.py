"""Create a gui for the bot.
    BUTTONS:
        - Add New Game: When clicked, the user will be asked to enter the name of the game in a small popup window that will allow the user to type the name of the game, if it doesn't already exist, the program creates a folder with the name of the game in the games folder.
            - In this folder it will also create a config file for the game with the name of the game and a .json extension.
        - Run: When clicked, the bot will run the bot and begin the process of automating the game.
        - Quit: When clicked, the program will quit.
    DROPDOWN MENUS:
        - Game: When clicked, a dropdown menu will appear with all the games that have been added to the bot.
        - Window: When clicked, a dropdown menu will appear with all the open windows on the computer.
    CHECKBOXES:
        - First Run: When checked, the bot will run the setup gui to get all necessary information from the user to automate the game.
    TEXT BOXES:
        - Goal: When clicked, the user will be able to type the goal of the game.
    LABELS: 
        - Game: A label that says "Game".
        - Window: A label that says "Window".
        - Goal: A label that says "Goal".
"""