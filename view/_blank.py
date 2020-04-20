# Imports
import tkinter as tk
from tkinter import *


# Class to ...
class _Blank:

    # Construct method
    def __init__(self, *args, **kwargs):
        # Attributes
        self.background_color = "#212121"
        self.text_color = "#e0e0e0"

        # Window Definition
        self.screen = tk.Tk()
        self.screen.title("RP Assignment: ...")
        self.screen['bg'] = self.background_color
        self.screen.geometry("600x400")
        self.screen.tk_setPalette(
            background=self.background_color,
            foreground=self.text_color)

    # Method to create the screen design and display it
    def show(self, controller):
        # Execute the screen
        self.screen.mainloop()

    # Method to destroy this screen
    def dismiss(self):
        # Destroy the screen
        self.screen.destroy()
