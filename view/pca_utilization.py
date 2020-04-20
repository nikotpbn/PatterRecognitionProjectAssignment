# Imports
import tkinter as tk
from tkinter import *


# Class to decide to use or not use PCA
class PCAUtilization:

    # Construct method
    def __init__(self, *args, **kwargs):
        # Attributes
        self.background_color = "#212121"
        self.text_color = "#e0e0e0"

        # Window Definition
        self.screen_pca_utilization = tk.Tk()
        self.screen_pca_utilization.title("RP Assignment: PCA Utilization")
        self.screen_pca_utilization['bg'] = self.background_color
        self.screen_pca_utilization.geometry("600x400")
        self.screen_pca_utilization.tk_setPalette(
            background=self.background_color,
            foreground=self.text_color)

    # Method to create the screen design and display it
    def show(self, controller):

        # Execute the screen
        self.screen_pca_utilization.mainloop()

    # Method to destroy this screen
    def dismiss(self):
        # Destroy the screen
        self.screen_pca_utilization.destroy()
