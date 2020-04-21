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

        # Window Definition for PCA Utilization
        self.screen_pca_utilization = tk.Tk()
        self.screen_pca_utilization.title("RP Assignment: PCA Utilization")
        self.screen_pca_utilization['bg'] = self.background_color
        self.screen_pca_utilization.geometry("600x400")
        self.screen_pca_utilization.tk_setPalette(
            background=self.background_color,
            foreground=self.text_color)

    # Method to create the screen design and display it
    def show(self, controller, number_feature):
        # Label to show the title in the screen_pca_utilization
        lb_title = Label(
            self.screen_pca_utilization,
            text="It was chosen the " + str(number_feature) + " (best) of 91 features with the feature\n selection method "
                 + controller.data.feature_selection_method_str + " for " + str(controller.data.scenario_selected_str) +
                 ".\n\nAfter that it was applied the feature reduction through the\n correlation matrix, finally " +
                 "holding " + str(len(controller.data.dataset["label"])) + " of " + str(number_feature) + " features.\n\n"
                 + "The next step is choose if you want to run the PCA or\n if you want go directly to the classifiers.",
            font=13)
        lb_title.config(anchor=CENTER)
        lb_title.pack(pady=15)
        # Button to see the features maintained
        button1 = Button(
            self.screen_pca_utilization,
            text="See features",
            command=lambda: self.show_features(controller))
        button1.config(height=1, width=50)
        button1.pack(pady=10)
        # Button to execute PCA
        button2 = Button(
            self.screen_pca_utilization,
            text="Run PCA Analisys",
            command=controller.run_pca_analisys)
        button2.config(height=3, width=50)
        button2.pack(pady=5)
        # Button to go to the classifiers
        button3 = Button(
            self.screen_pca_utilization,
            text="Skip PCA",
            command=lambda: controller.choose_classifier(0))
        button3.config(height=3, width=50)
        button3.pack(pady=5)

        # Execute the screen
        self.screen_pca_utilization.mainloop()

    def show_features(self, controller):
        # Window Definition to show features
        screen_show_features = tk.Tk()
        screen_show_features.title("RP Assignment: Show features")
        screen_show_features['bg'] = self.background_color
        screen_show_features.geometry("230x700")
        screen_show_features.tk_setPalette(
            background=self.background_color,
            foreground=self.text_color)

        # Prepare the string to be displayed as feature maintained
        str_features_maintained = ""
        for feature in controller.data.dataset["label"]:
            str_features_maintained += feature + "\n"

        # Prepare the string to be displayed as feature excluded
        str_features_excluded = ""
        for feature in controller.data.features_excluded_by_feature_reduction:
            str_features_excluded += feature + "\n"

        # Label to show the maintained features
        lb_features_maintained = Label(
            screen_show_features,
            text="Features saved")
        lb_features_maintained.config(anchor=CENTER)
        lb_features_maintained.grid(row=0, column=0, padx=(20, 0), pady=(10, 0))

        # Label to show the maintained features
        lb_features_maintained = Label(
            screen_show_features,
            text="Features excluded")
        lb_features_maintained.config(anchor=CENTER)
        lb_features_maintained.grid(row=0, column=1, padx=(20, 0), pady=(10, 0))

        # Label to show the maintained features
        lb_features_maintained = Label(
            screen_show_features,
            text=str_features_maintained)
        lb_features_maintained.config(anchor=CENTER)
        lb_features_maintained.grid(row=1, column=0, padx=(20, 0), pady=(10, 0))

        # Label to show the deleted features
        lb_features_excluded = Label(
            screen_show_features,
            text=str_features_excluded)
        lb_features_excluded.config(anchor=CENTER)
        lb_features_excluded.grid(row=1, column=1, padx=(20, 0), pady=(10, 0))

        # Execute the screen
        screen_show_features.mainloop()

    # Method to destroy this screen
    def dismiss(self):
        # Destroy the screen
        self.screen_pca_utilization.destroy()
