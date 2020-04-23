# Imports
import tkinter as tk
from tkinter import *


# Class to select the configurations of the feature selection
class FeatureSelectionAndReduction:

    # Construct method
    def __init__(self, *args, **kwargs):
        # Attributes
        self.background_color = "#212121"
        self.text_color = "#e0e0e0"

        # Window Definition
        self.feature_selection_screen = tk.Tk()
        self.feature_selection_screen.title("RP Assignment: Feature Selection")
        self.feature_selection_screen['bg'] = self.background_color
        self.feature_selection_screen.geometry("600x400")
        self.feature_selection_screen.tk_setPalette(
            background=self.background_color,
            foreground=self.text_color)

    # Method to create the screen design and display it
    def show(self, controller):
        # Label to show the title in the feature_selection_screen
        lb_title = Label(
            self.feature_selection_screen,
            text="The dataset '" + controller.data.database_selected_str + "' was selected\n and the pre-processing of "
                 + "scenario '" + controller.data.scenario_selected_str + "'\n was applied.",
            font=13)
        lb_title.config(anchor=CENTER)
        lb_title.pack(pady=15)

        # Method of Feature Selection
        opt_feature_selection = IntVar()
        feature_selection_frame = LabelFrame(
            self.feature_selection_screen,
            text="   Choose the selection method   ",
            labelanchor='n')
        feature_selection_frame.pack(pady=15)
        rb_feature_selection1 = Radiobutton(
            feature_selection_frame,
            variable=opt_feature_selection,
            value=1,
            text="K-bests",
            selectcolor=self.background_color)
        rb_feature_selection1.pack()
        rb_feature_selection2 = Radiobutton(
            feature_selection_frame,
            variable=opt_feature_selection,
            value=2,
            text="Kruskal-Wallis",
            selectcolor=self.background_color)
        rb_feature_selection2.select()
        rb_feature_selection2.pack()
        # Numbers of features to be used
        feature_reduction_frame = LabelFrame(
            self.feature_selection_screen,
            text="   Select the number of features to be used   ",
            labelanchor='n')
        feature_reduction_frame.pack(pady=15)
        number_feature = Scale(
            feature_reduction_frame,
            from_=2,
            to=91,
            orient=HORIZONTAL,
            sliderlength=15,
            length=400,
            tickinterval=10)
        number_feature.set(91)
        number_feature.pack()
        # Execute button
        button1 = Button(self.feature_selection_screen,
                         text="Run Feature Selection and Feature Reduction",
                         command=lambda: controller.feature_selection_and_reduction(
                             opt_feature_selection.get(),
                             number_feature.get()
                         ))
        button1.config(height=3, width=50)
        button1.pack(pady=15)

        # Execute the screen
        self.feature_selection_screen.mainloop()

    # Method to destroy this screen
    def dismiss(self):
        # Destroy the screen
        self.feature_selection_screen.destroy()
