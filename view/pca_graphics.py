# Imports
import numpy as np
import tkinter as tk
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Interface to show the PCA graphics, and decide how many features must be maintained
class PCAGraphics:
    # Constructor Method
    def __init__(self, *args, **kwargs):
        # Attributes
        self.background_color = "#212121"
        self.text_color = "#e0e0e0"

        # Window Definition
        self.screen_pca_graphics = tk.Tk()
        self.screen_pca_graphics.title("RP Assignment: ...")
        self.screen_pca_graphics['bg'] = self.background_color
        self.screen_pca_graphics.geometry("945x560")
        self.screen_pca_graphics.tk_setPalette(
            background=self.background_color,
            foreground=self.text_color)

    # Method to create the screen design and display it
    def show(self, controller, explained_variance_, x_values, singular_values_):
        # Label to show the title in the screen_pca_graphics
        label1 = Label(
            self.screen_pca_graphics,
            text="Result of PCA Analisys",
            font=20)
        label1.config(anchor=CENTER)
        label1.grid(row=0, column=0, columnspan=2, pady=15)

        # Create the graphics (Eigenvalues x Principal Components) and plot it into the screen
        figure1 = plt.Figure(figsize=(6, 4), dpi=75)
        ax1 = figure1.add_subplot(111)
        ax1.scatter(x_values, singular_values_, color='g')
        ax1.set_title('Principal Component Analysis (PCA)')
        ax1.set_xlabel('Principal Components')
        ax1.set_ylabel('Eigenvalues')
        scatter1 = FigureCanvasTkAgg(figure1, self.screen_pca_graphics)
        scatter1.get_tk_widget().grid(row=1, column=0, padx=(15, 0), pady=(10, 0))

        # Create the graphics (Eigenvalues x Principal Components) and plot it into the screen
        figure2 = plt.Figure(figsize=(6, 4), dpi=75)
        ax2 = figure2.add_subplot(111)
        ax2.scatter(x_values, (np.cumsum(explained_variance_)/sum(explained_variance_))*100, color='g')
        ax2.set_title('Principal Component Analysis (PCA)')
        ax2.set_xlabel('Principal Components')
        ax2.set_ylabel('Percentage of variance')
        scatter2 = FigureCanvasTkAgg(figure2, self.screen_pca_graphics)
        scatter2.get_tk_widget().grid(row=1, column=1, padx=(15, 0), pady=(10, 0))

        # Feature Selection Options
        pca_frame = LabelFrame(
            self.screen_pca_graphics,
            text="   Select the number of features   ",
            labelanchor='n')
        pca_frame.grid(row=2, column=0, columnspan=2, pady=15)
        scale1 = Scale(
            pca_frame,
            from_=2,
            to=len(controller.data.dataset["label"]),
            orient=HORIZONTAL,
            sliderlength=15,
            length=400,
            tickinterval=5)
        scale1.pack()

        # Button to execute PCA
        button1 = Button(
            self.screen_pca_graphics,
            text="Run PCA",
            command=lambda: controller.choose_classifier(scale1.get())
        )
        button1.config(height=3, width=50)
        button1.grid(row=3, column=0, columnspan=2, pady=15)

        # Execute the screen
        self.screen_pca_graphics.mainloop()

    # Method to destroy this screen
    def dismiss(self):
        # Destroy the screen
        self.screen_pca_graphics.destroy()
