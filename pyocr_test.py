# Take a screenshot of the desktop and save it as a .png file.

import pyautogui
import time
import os
import json
import cv2
import numpy as np
import pyocr
import pyocr.builders
import pyocr.tesseract
import pytesseract
import tkinter as tk
from tkinter import ttk

"""
Simple gui with a dropdown menu that lists all open windows that are visible and have a title on the computer. A button that when clicked will take a screenshot of the window that is selected in the dropdown menu and save it as a .png file and display it in a window that the user can use a square selection tool to select the game board and save it as a .png file.
"""

# The gui
class Gui:
    