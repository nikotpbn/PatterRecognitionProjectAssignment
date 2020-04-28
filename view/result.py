# Imports
import tkinter as tk
from tkinter import *


# Interface to show the result
class Result:
    # Constructor Method
    def __init__(self, *args, **kwargs):
        # Attributes
        self.background_color = "#212121"
        self.text_color = "#e0e0e0"

        # Window Definition
        self.screen_result = tk.Tk()
        self.screen_result.title("RP Assignment: Results")
        self.screen_result['bg'] = self.background_color
        self.screen_result.geometry("600x400")
        self.screen_result.tk_setPalette(
            background=self.background_color,
            foreground=self.text_color)

    # Method to create the screen design and display it
    def show(self, controller, classifier, cm_derivations):
        # String preparations
        mean_error = ""
        sensitivity = ""
        specificity = ""
        classifier_label = ""

        if classifier == 1:
            classifier_label = "These are the results found by the\n classifier Minimum Distance Classifier (MDC)"
            mean_error = "Mean of errors for MDC: " + "{0:.2%}".format(cm_derivations["misclassification"])
            sensitivity = "True positive ratio for MDC: " + "{0:.2}".format(cm_derivations["sensitivity"])
            specificity = "False positive ratio for MDC: " + "{0:.2}".format(cm_derivations["specificity"])
        elif classifier == 2:
            classifier_label = "These are the results found by the\n " \
                               "classifier Fisher Discriminant Analisys (Fisher LDA)"
            mean_error = "Mean of errors Fisher LDA: " + "{0:.2%}".format(cm_derivations["misclassification"])
            sensitivity = "True positive ratio Fisher LDA: " + "{0:.2}".format(cm_derivations["sensitivity"])
            specificity = "False positive ratio Fisher LDA: " + "{0:.2}".format(cm_derivations["specificity"])
        elif classifier == 3:
            classifier_label = "These are the results found by the\n classifier K nearest neighbors (KNN)"
            mean_error = "Mean of errors KNN: " + "{0:.2%}".format(cm_derivations["misclassification"])
            sensitivity = "True positive ratio KNN: " + "{0:.2}".format(cm_derivations["sensitivity"])
            specificity = "False positive ratio KNN: " + "{0:.2}".format(cm_derivations["specificity"])
        elif classifier == 4:
            classifier_label = "These are the results found by the\n classifier Naive-Bayes"
            mean_error = "Mean of errors Naive-Bayes: " + "{0:.2%}".format(cm_derivations["misclassification"])
            sensitivity = "True positive ratio Naive-Bayes: " + "{0:.2}".format(cm_derivations["sensitivity"])
            specificity = "False positive ratio Naive-Bayes: " + "{0:.2}".format(cm_derivations["specificity"])
        elif classifier == 5:
            classifier_label = "These are the results found by the\n classifier Support Vector Machine (SVM)"
            mean_error = "Mean of errors SVM: " + "{0:.2%}".format(cm_derivations["misclassification"])
            sensitivity = "True positive ratio SVM: " + "{0:.2}".format(cm_derivations["sensitivity"])
            specificity = "False positive ratio SVM: " + "{0:.2}".format(cm_derivations["specificity"])

        # Information Add
        label1 = Label(self.screen_result, text=classifier_label, font=20)
        label1.config(anchor=CENTER)
        label1.pack(pady=15)

        label2 = Label(self.screen_result, text=mean_error, font=20)
        label2.config(anchor=CENTER)
        label2.pack(pady=15)

        label3 = Label(self.screen_result, text=sensitivity, font=20)
        label3.config(anchor=CENTER)
        label3.pack(pady=15)

        label4 = Label(self.screen_result, text=specificity, font=20)
        label4.config(anchor=CENTER)
        label4.pack(pady=15)

        # TODO: Restart Application
        # button1 = Button(self.screen_result, text="Restart Application")
        # button1.config(height=3, width=50)
        # button1.pack(pady=15)

        # Execute the screen
        self.screen_result.mainloop()

    # Method to destroy this screen
    def dismiss(self):
        # Destroy the screen
        self.screen_result.destroy()
