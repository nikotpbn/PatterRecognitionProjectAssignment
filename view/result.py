# Imports
import numpy as np
import tkinter as tk
from tkinter import *
from tkinter import ttk


# Function to set label on a given screen
def add_label(tab, text):
    label = Label(tab, text=text, font=20)
    label.config(anchor=CENTER)
    label.pack(pady=15)

    return label


# Function to get results from performance dict using activity_id
def get_results(performance, activity_id):
    misclassification_per_cent = (performance["avg_misclassification"][activity_id] * 100)
    # misclassification = performance["avg_misclassification"][activity_id].astype(np.str)
    mean = "Mean of error: %.2f" % misclassification_per_cent
    mean += "".join("% \n")

    tpr_per_cent = performance["sensitivity"][activity_id] * 100
    # tpr = performance["sensitivity"][activity_id].astype(np.str)
    sensitivity = "True Positive Ratio (TPR | Sensitivity): %.2f" % tpr_per_cent
    sensitivity += "".join("% \n")

    tnr_per_cent = performance["specificity"][activity_id] * 100
    # tnr = performance["specificity"][activity_id].astype(np.str)
    specificity = "True Negative Ratio (TNR | Specificity): %.2f" % tnr_per_cent
    specificity += "".join("% \n")

    return mean, sensitivity, specificity


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

        self.tab_parent = ttk.Notebook(self.screen_result)

    # Method to create the screen design and display it
    def show(self, controller, classifier, performance, scenario):
        # String preparations
        mean_error = ""
        sensitivity = ""
        specificity = ""
        classifier_label = ""

        if scenario == 1:
            if classifier == 1:
                classifier_label = "These are the results found by the\n classifier Minimum Distance Classifier (MDC)"
                mean_error = "Mean of errors for MDC: %.2f" % (performance["avg_misclassification"] * 100)
                sensitivity = "True positive ratio for MDC: %.2f" % (performance["sensitivity"] * 100)
                specificity = "True negative ratio for MDC: %.2f" % (performance["specificity"] * 100)
            elif classifier == 2:
                classifier_label = "These are the results found by the\n " \
                                   "classifier Fisher Discriminant Analisys (Fisher LDA)"
                mean_error = "Mean of errors Fisher LDA: %.2f" % (performance["avg_misclassification"] * 100)
                sensitivity = "True positive ratio Fisher LDA: %.2f" % (performance["sensitivity"] * 100)
                specificity = "True negativeratio Fisher LDA: %.2f" % (performance["specificity"] * 100)
            elif classifier == 3:
                classifier_label = "These are the results found by the\n classifier K nearest neighbors (KNN)"
                mean_error = "Mean of errors KNN: %.2f" % (performance["avg_misclassification"] * 100)
                sensitivity = "True positive ratio KNN: %.2f" % (performance["sensitivity"] * 100)
                specificity = "True negative ratio KNN: %.2f" % (performance["specificity"] * 100)
            elif classifier == 4:
                classifier_label = "These are the results found by the\n classifier Naive-Bayes"
                mean_error = "Mean of errors Naive-Bayes: %.2f" % (performance["avg_misclassification"] *100)
                sensitivity = "True positive ratio Naive-Bayes: %.2f" % (performance["sensitivity"] * 100)
                specificity = "True negative ratio Naive-Bayes: %.2f" % (performance["specificity"] * 100)
            elif classifier == 5:
                classifier_label = "These are the results found by the\n classifier Support Vector Machine (SVM)"
                mean_error = "Mean of errors SVM: %.2f" % (performance["avg_misclassification"] * 100)
                sensitivity = "True positive ratio SVM: %.2f" % (performance["sensitivity"] * 100)
                specificity = "True negative ratio SVM: %.2f" % (performance["specificity"] * 100)

            mean_error += "".join("% \n")
            sensitivity += "".join("% \n")
            specificity += "".join("% \n")

            # Information Add
            add_label(self.screen_result, classifier_label)
            add_label(self.screen_result, mean_error)
            add_label(self.screen_result, sensitivity)
            add_label(self.screen_result, specificity)

        else:
            # activity_id:
            # 1 = A
            # 2 = B
            # 3 = C
            # ...
            # 18 = S

            # Variables
            # Set the number of classes based on the scenario
            if scenario == 2:
                n_classes = 3

            else:
                n_classes = 18
                # Readjust screen size for scenario C to show all tabs
                self.screen_result.geometry("1100x400")

            labels = []
            tabs = [tk.Frame(self.tab_parent) for i in range(n_classes)]
            activity_label = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                              'K', 'L', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', ]

            # Set labels based on classifier choice
            if classifier == 1:
                for i in range(0, n_classes):
                    labels.append("Class %s results for MDC (Minimum Distance Classifier)" % activity_label[i])

            elif classifier == 2:
                for i in range(0, n_classes):
                    labels.append("Class %s results for FLDA (Fisher Discriminant Analysis)" % activity_label[i])

            elif classifier == 3:
                for i in range(0, n_classes):
                    labels.append("Class %s results for KNN (K Nearest Neighbors)" % activity_label[i])

            elif classifier == 4:
                for i in range(0, n_classes):
                    labels.append("Class %s results for Naive-Bayes" % activity_label[i])

            elif classifier == 5:
                for i in range(0, n_classes):
                    labels.append("Class %s results for SVM (Support Vector Machine)" % activity_label[i])

            for i in range(0, n_classes):
                # Get and Set results for all tabs
                mean_error, sensitivity, specificity = get_results(performance, i)
                add_label(tabs[i], labels[i])
                add_label(tabs[i], mean_error)
                add_label(tabs[i], sensitivity)
                add_label(tabs[i], specificity)

                # Add tabs to parent container
                text = "Class %s" % activity_label[i]
                self.tab_parent.add(tabs[i], text=text)

            # Pack tabs into parent container
            self.tab_parent.pack(expand=1, fill='both')

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

