"""2248_BOT#######################################################################################################
    This is the main file of the bot.
    This bot is for the automation of the game 2248.
    
    THE GUI:
        The gui will be created using the tkinter module.
        The gui will have a title of "2248 Bot".
        The gui will have a size of 500x500.
        The gui will have a dropdown list that will list all open and visible windows on the computer.
        The gui will have a button labeled "Run" that will run the bot.
        The gui will have a button labeled "Quit" that will quit the program.
        A button labeled "Run Setup" that will run the setup that will assist the user in preparing screenshots of the game board and game window for the bot to use.
        
    THE SETUP:
        The setup will be run if the user clicks the "Run Setup" button.

    THE BOT:
        The main loop of the bot will be as follows:
        - Launch the gui and wait for the user to choos a window and press the run button.
        - Take a screenshot of the game window and crop it to the game board.
        - Use the screenshot of the game board to determine the current state of the game board.
        - The current state of the game board will be determined using opencv to detect that the game_board is visible on the screen.
        - If it is not visible, the bot will continue to take screenshots and search for the game board to know when the game board is visible, the image of the "X" used to close ads that will play from time to time, or the image of the game over screen, or the image of the main menu screen and respond accordingly.
        GAME STATES:
            MAIN MENU:
                - If the bot detects the main menu screen, it will click the "Play" button.
            GAME OVER:
                - If the bot detects the game over screen, it will click the "Play Again" button.
            AD:
                - If the bot detects the ad, it will click the "X" button to close the ad.
            GAME BOARD:
                - If the bot detects the game board, it will take a screenshot of the game board and crop it to the game board.

    THE GAME BOARD:
        - The game board will be a grid of 8 rows and 5 columns.
        - The game board information will be stored in a list of dictionaries.
        - Each dictionary will contain the following information:
            - The row and column number. Rows being A-H and columns being 1-5.
            - The number value of the tile as read by pyocr.
            - A list of adjacent tiles.
            - The coordinates of the center of the tile.
        - The game board will be updated after every move.
            
            
"""###############################################################################################################

"""GUI############################################################################################################
Create a gui for the bot.
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
"""###############################################################################################################

"""SETUP##########################################################################################################


"""###############################################################################################################