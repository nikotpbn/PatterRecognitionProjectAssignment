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
    misclassification = performance["avg_misclassification"][activity_id].astype(np.str)
    mean = "Mean of error: \n"
    mean += "".join(misclassification)

    tpr = performance["sensitivity"][activity_id].astype(np.str)
    sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
    sensitivity += "".join(tpr)

    tnr = performance["specificity"][activity_id].astype(np.str)
    specificity = "True Negative Ratio (TNR | Specificity): \n"
    specificity += "".join(tnr)

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
                mean_error = "Mean of errors for MDC: " + "{0:.2%}".format(performance["avg_misclassification"])
                sensitivity = "True positive ratio for MDC: " + "{0:.2}".format(performance["sensitivity"])
                specificity = "True negative ratio for MDC: " + "{0:.2}".format(performance["specificity"])
            elif classifier == 2:
                classifier_label = "These are the results found by the\n " \
                                   "classifier Fisher Discriminant Analisys (Fisher LDA)"
                mean_error = "Mean of errors Fisher LDA: " + "{0:.2%}".format(performance["avg_misclassification"])
                sensitivity = "True positive ratio Fisher LDA: " + "{0:.2}".format(performance["sensitivity"])
                specificity = "True negativeratio Fisher LDA: " + "{0:.2}".format(performance["specificity"])
            elif classifier == 3:
                classifier_label = "These are the results found by the\n classifier K nearest neighbors (KNN)"
                mean_error = "Mean of errors KNN: " + "{0:.2%}".format(performance["avg_misclassification"])
                sensitivity = "True positive ratio KNN: " + "{0:.2}".format(performance["sensitivity"])
                specificity = "True negative ratio KNN: " + "{0:.2}".format(performance["specificity"])
            elif classifier == 4:
                classifier_label = "These are the results found by the\n classifier Naive-Bayes"
                mean_error = "Mean of errors Naive-Bayes: " + "{0:.2%}".format(performance["avg_misclassification"])
                sensitivity = "True positive ratio Naive-Bayes: " + "{0:.2}".format(performance["sensitivity"])
                specificity = "True negative ratio Naive-Bayes: " + "{0:.2}".format(performance["specificity"])
            elif classifier == 5:
                classifier_label = "These are the results found by the\n classifier Support Vector Machine (SVM)"
                mean_error = "Mean of errors SVM: " + "{0:.2%}".format(performance["avg_misclassification"])
                sensitivity = "True positive ratio SVM: " + "{0:.2}".format(performance["sensitivity"])
                specificity = "True negative ratio SVM: " + "{0:.2}".format(performance["specificity"])

            # Information Add
            add_label(self.screen_result, classifier_label)
            add_label(self.screen_result, mean_error)
            add_label(self.screen_result, sensitivity)
            add_label(self.screen_result, specificity)

        elif scenario == 2:
            # TODO: Describe activity per id (it is used with get_results function)
            # activity_id:
            # 0 = A
            # 1 = B
            # 2 = C

            # Variables
            label_a = ""
            label_b = ""
            label_c = ""

            # Interface tabs to show results per class
            tab1 = tk.Frame(self.tab_parent)
            tab2 = tk.Frame(self.tab_parent)
            tab3 = tk.Frame(self.tab_parent)

            # Set labels based on classifier choice
            if classifier == 1:
                label_a = "Class A results for MDC (Minimum Distance Classifier)"
                label_b = "Class B results for MDC (Minimum Distance Classifier)"
                label_c = "Class C results for MDC (Minimum Distance Classifier)"

            elif classifier == 2:
                label_a = "Class A results for FLDA (Fisher Discriminant Analysis)"
                label_b = "Class B results for FLDA (Fisher Discriminant Analysis)"
                label_c = "Class C results for FLDA (Fisher Discriminant Analysis)"

            elif classifier == 3:
                label_a = "Class A results for KNN (K Nearest Neighbors)"
                label_b = "Class B results for KNN (K Nearest Neighbors)"
                label_c = "Class C results for KNN (K Nearest Neighbors)"

            elif classifier == 4:
                label_a = "Class A results for Naive-Bayes"
                label_b = "Class B results for Naive-Bayes"
                label_c = "Class C results for Naive-Bayes"

            elif classifier == 5:
                label_a = "Class A results for SVM (Support Vector Machine)"
                label_b = "Class B results for SVM (Support Vector Machine)"
                label_c = "Class C results for SVM (Support Vector Machine)"

            # Get results from performance dict using activity_id
            mean_error_a, sensitivity_a, specificity_a = get_results(performance, 0)
            mean_error_b, sensitivity_b, specificity_b = get_results(performance, 1)
            mean_error_c, sensitivity_c, specificity_c = get_results(performance, 2)

            # Set labels inside tab 1
            add_label(tab1, label_a)
            add_label(tab1, mean_error_a)
            add_label(tab1, sensitivity_a)
            add_label(tab1, specificity_a)

            # Set labels inside tab 2
            add_label(tab2, label_b)
            add_label(tab2, mean_error_b)
            add_label(tab2, sensitivity_b)
            add_label(tab2, specificity_b)

            # Set labels inside tab 3
            add_label(tab3, label_c)
            add_label(tab3, mean_error_c)
            add_label(tab3, sensitivity_c)
            add_label(tab3, specificity_c)

            # Add tabs to parent container
            self.tab_parent.add(tab1, text="Class A")
            self.tab_parent.add(tab2, text="Class B")
            self.tab_parent.add(tab3, text="Class C")

            # Pack tabs into parent container
            self.tab_parent.pack(expand=1, fill='both')

        else:
            # activity_id:
            # 1 = A
            # 2 = B
            # 3 = C
            # ...
            # 18 = S

            # Variables
            labels = []
            tabs = [tk.Frame(self.tab_parent) for i in range(18)]
            activity_label = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                              'K', 'L', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', ]

            # Set labels based on classifier choice
            if classifier == 1:
                for i in range(0, 18):
                    labels.append("Class %s results for MDC (Minimum Distance Classifier)" % activity_label[i])

            elif classifier == 2:
                for i in range(0, 18):
                    labels.append("Class %s results for FLDA (Fisher Discriminant Analysis)" % activity_label[i])

            elif classifier == 3:
                for i in range(0, 18):
                    labels.append("Class %s results for KNN (K Nearest Neighbors)" % activity_label[i])

            elif classifier == 4:
                for i in range(0, 18):
                    labels.append("Class %s results for Naive-Bayes" % activity_label[i])

            elif classifier == 5:
                for i in range(0, 18):
                    labels.append("Class %s results for SVM (Support Vector Machine)" % activity_label[i])

            for i in range(0, 18):
                # Get and Set results for all tabs
                mean_error, sensitivity, specificity = get_results(performance, i)
                add_label(tabs[i], labels[i])
                add_label(tabs[i], mean_error)
                add_label(tabs[i], sensitivity)
                add_label(tabs[i], specificity)

                # Add tabs to parent container
                text = "Class %s" % activity_label[i]
                self.tab_parent.add(tabs[i], text=text)

            # Readjust screen size
            self.screen_result.geometry("1100x400")

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

