# Imports
import numpy as np
import tkinter as tk
from tkinter import *
from tkinter import ttk


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
    def show(self, controller, classifier, cm_derivations, scenario):
        # String preparations
        mean_error = ""
        sensitivity = ""
        specificity = ""
        classifier_label = ""

        if scenario == 1:
            if classifier == 1:
                classifier_label = "These are the results found by the\n classifier Minimum Distance Classifier (MDC)"
                mean_error = "Mean of errors for MDC: " + "{0:.2%}".format(cm_derivations["avg_misclassification"])
                sensitivity = "True positive ratio for MDC: " + "{0:.2}".format(cm_derivations["sensitivity"])
                specificity = "True negative ratio for MDC: " + "{0:.2}".format(cm_derivations["specificity"])
            elif classifier == 2:
                classifier_label = "These are the results found by the\n " \
                                   "classifier Fisher Discriminant Analisys (Fisher LDA)"
                mean_error = "Mean of errors Fisher LDA: " + "{0:.2%}".format(cm_derivations["avg_misclassification"])
                sensitivity = "True positive ratio Fisher LDA: " + "{0:.2}".format(cm_derivations["sensitivity"])
                specificity = "True negativeratio Fisher LDA: " + "{0:.2}".format(cm_derivations["specificity"])
            elif classifier == 3:
                classifier_label = "These are the results found by the\n classifier K nearest neighbors (KNN)"
                mean_error = "Mean of errors KNN: " + "{0:.2%}".format(cm_derivations["avg_misclassification"])
                sensitivity = "True positive ratio KNN: " + "{0:.2}".format(cm_derivations["sensitivity"])
                specificity = "True negative ratio KNN: " + "{0:.2}".format(cm_derivations["specificity"])
            elif classifier == 4:
                classifier_label = "These are the results found by the\n classifier Naive-Bayes"
                mean_error = "Mean of errors Naive-Bayes: " + "{0:.2%}".format(cm_derivations["avg_misclassification"])
                sensitivity = "True positive ratio Naive-Bayes: " + "{0:.2}".format(cm_derivations["sensitivity"])
                specificity = "True negative ratio Naive-Bayes: " + "{0:.2}".format(cm_derivations["specificity"])
            elif classifier == 5:
                classifier_label = "These are the results found by the\n classifier Support Vector Machine (SVM)"
                mean_error = "Mean of errors SVM: " + "{0:.2%}".format(cm_derivations["avg_misclassification"])
                sensitivity = "True positive ratio SVM: " + "{0:.2}".format(cm_derivations["sensitivity"])
                specificity = "True negative ratio SVM: " + "{0:.2}".format(cm_derivations["specificity"])

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

        elif scenario == 2:
            # Interface tabs to show results per class
            tab1 = tk.Frame(self.tab_parent)
            tab2 = tk.Frame(self.tab_parent)
            tab3 = tk.Frame(self.tab_parent)

            if classifier == 1:
                # ######################## TAB 1 -> Class A results ##################################
                classifier_label = "These are the results found by the\n classifier Minimum Distance Classifier (MDC)" \
                                   "for Class A"
                misclassification = cm_derivations["avg_misclassification"][0].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][0].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][0].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab1, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab1, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab1, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab1, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 2 -> Class B results ##################################
                classifier_label = "These are the results found by the\n classifier Minimum Distance Classifier (MDC)" \
                                   "for Class B"
                misclassification = cm_derivations["avg_misclassification"][1].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][1].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][1].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab2, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab2, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab2, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab2, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 3 -> Class C results ##################################
                classifier_label = "These are the results found by the\n classifier Minimum Distance Classifier (MDC)" \
                                   "for Class C"
                misclassification = cm_derivations["avg_misclassification"][2].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][2].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][2].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab3, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab3, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab3, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab3, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

            elif classifier == 2:
                # ######################## TAB 1 -> Class A results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier Fisher Discriminant Analisys (Fisher LDA) for Class A"
                misclassification = cm_derivations["avg_misclassification"][0].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][0].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][0].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab1, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab1, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab1, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab1, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 2 -> Class B results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier Fisher Discriminant Analisys (Fisher LDA) for Class B"
                misclassification = cm_derivations["avg_misclassification"][1].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][1].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][1].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab2, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab2, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab2, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab2, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 3 -> Class C results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier Fisher Discriminant Analisys (Fisher LDA) for Class C"
                misclassification = cm_derivations["avg_misclassification"][2].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][2].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][2].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab3, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab3, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab3, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab3, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

            elif classifier == 3:
                # ######################## TAB 1 -> Class A results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier K nearest neighbors (KNN) for Class A"
                misclassification = cm_derivations["avg_misclassification"][0].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][0].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][0].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab1, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab1, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab1, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab1, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 2 -> Class B results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier K nearest neighbors (KNN) for Class B"
                misclassification = cm_derivations["avg_misclassification"][1].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][1].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][1].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab2, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab2, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab2, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab2, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 3 -> Class C results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier K nearest neighbors (KNN) for Class C"
                misclassification = cm_derivations["avg_misclassification"][2].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][2].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][2].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab3, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab3, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab3, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab3, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

            elif classifier == 4:
                # ######################## TAB 1 -> Class A results ##################################
                classifier_label = "These are the results found by the\n classifier Naive-Bayes for Class A"
                misclassification = cm_derivations["avg_misclassification"][0].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][0].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][0].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab1, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab1, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab1, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab1, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 2 -> Class B results ##################################
                classifier_label = "These are the results found by the\n classifier Naive-Bayes for Class B"
                misclassification = cm_derivations["avg_misclassification"][1].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][1].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][1].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab2, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab2, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab2, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab2, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 3 -> Class C results ##################################
                classifier_label = "These are the results found by the\n classifier Naive-Bayes for Class C"
                misclassification = cm_derivations["avg_misclassification"][2].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][2].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][2].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab3, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab3, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab3, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab3, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

            elif classifier == 5:
                # ######################## TAB 1 -> Class A results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier Support Vector Machine (SVM) for Class A"
                misclassification = cm_derivations["avg_misclassification"][0].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][0].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][0].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab1, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab1, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab1, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab1, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 2 -> Class B results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier Support Vector Machine (SVM) for Class B"
                misclassification = cm_derivations["avg_misclassification"][1].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][1].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][1].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab2, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab2, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab2, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab2, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 3 -> Class C results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier Support Vector Machine (SVM) for Class C"
                misclassification = cm_derivations["avg_misclassification"][2].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][2].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][2].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab3, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab3, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab3, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab3, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

            # Add tabs to parent container
            self.tab_parent.add(tab1, text="Class A")
            self.tab_parent.add(tab2, text="Class B")
            self.tab_parent.add(tab3, text="Class C")

            # Pack tabs into parent container
            self.tab_parent.pack(expand=1, fill='both')

        else:
            # Interface tabs to show results per class
            tab1 = tk.Frame(self.tab_parent)
            tab2 = tk.Frame(self.tab_parent)
            tab3 = tk.Frame(self.tab_parent)
            tab4 = tk.Frame(self.tab_parent)
            tab5 = tk.Frame(self.tab_parent)
            tab6 = tk.Frame(self.tab_parent)
            tab7 = tk.Frame(self.tab_parent)
            tab8 = tk.Frame(self.tab_parent)
            tab9 = tk.Frame(self.tab_parent)
            tab10 = tk.Frame(self.tab_parent)
            tab11 = tk.Frame(self.tab_parent)
            tab12 = tk.Frame(self.tab_parent)
            tab13 = tk.Frame(self.tab_parent)
            tab14 = tk.Frame(self.tab_parent)
            tab15 = tk.Frame(self.tab_parent)
            tab16 = tk.Frame(self.tab_parent)
            tab17 = tk.Frame(self.tab_parent)
            tab18 = tk.Frame(self.tab_parent)

            if classifier == 1:
                # ######################## TAB 1 -> Class A results ##################################
                classifier_label = "These are the results found by the\n classifier Minimum Distance Classifier (MDC)" \
                                   "for Class A"
                misclassification = cm_derivations["avg_misclassification"][0].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][0].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][0].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab1, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab1, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab1, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab1, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 2 -> Class B results ##################################
                classifier_label = "These are the results found by the\n classifier Minimum Distance Classifier (MDC)" \
                                   "for Class B"
                misclassification = cm_derivations["avg_misclassification"][1].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][1].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][1].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab2, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab2, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab2, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab2, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 3 -> Class C results ##################################
                classifier_label = "These are the results found by the\n classifier Minimum Distance Classifier (MDC)" \
                                   "for Class C"
                misclassification = cm_derivations["avg_misclassification"][2].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][2].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][2].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab3, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab3, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab3, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab3, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 4 -> Class D results ##################################
                classifier_label = "These are the results found by the\n classifier Minimum Distance Classifier (MDC)" \
                                   "for Class D"
                misclassification = cm_derivations["avg_misclassification"][3].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][3].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][3].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab4, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab4, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab4, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab4, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 5 -> Class E results ##################################
                classifier_label = "These are the results found by the\n classifier Minimum Distance Classifier (MDC)" \
                                   "for Class E"
                misclassification = cm_derivations["avg_misclassification"][4].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][4].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][4].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab5, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab5, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab5, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab5, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 6 -> Class F results ##################################
                classifier_label = "These are the results found by the\n classifier Minimum Distance Classifier (MDC)" \
                                   "for Class F"
                misclassification = cm_derivations["avg_misclassification"][5].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][5].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][5].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab6, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab6, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab6, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab6, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 7 -> Class G results ##################################
                classifier_label = "These are the results found by the\n classifier Minimum Distance Classifier (MDC)" \
                                   "for Class G"
                misclassification = cm_derivations["avg_misclassification"][6].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][6].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][6].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab7, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab7, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab7, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab7, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 8 -> Class H results ##################################
                classifier_label = "These are the results found by the\n classifier Minimum Distance Classifier (MDC)" \
                                   "for Class H"
                misclassification = cm_derivations["avg_misclassification"][7].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][7].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][7].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab8, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab8, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab8, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab8, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 9 -> Class I results ##################################
                classifier_label = "These are the results found by the\n classifier Minimum Distance Classifier (MDC)" \
                                   "for Class I"
                misclassification = cm_derivations["avg_misclassification"][8].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][8].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][8].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab9, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab9, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab9, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab9, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 10 -> Class J results ##################################
                classifier_label = "These are the results found by the\n classifier Minimum Distance Classifier (MDC)" \
                                   "for Class J"
                misclassification = cm_derivations["avg_misclassification"][9].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][9].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][9].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab10, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab10, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab10, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab10, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 11 -> Class K results ##################################
                classifier_label = "These are the results found by the\n classifier Minimum Distance Classifier (MDC)" \
                                   "for Class K"
                misclassification = cm_derivations["avg_misclassification"][10].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][10].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][10].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab11, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab11, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab11, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab11, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 12 -> Class L results ##################################
                classifier_label = "These are the results found by the\n classifier Minimum Distance Classifier (MDC)" \
                                   "for Class L"
                misclassification = cm_derivations["avg_misclassification"][11].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][11].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][11].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab12, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab12, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab12, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab12, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 13 -> Class M results ##################################
                classifier_label = "These are the results found by the\n classifier Minimum Distance Classifier (MDC)" \
                                   "for Class M"
                misclassification = cm_derivations["avg_misclassification"][12].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][12].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][12].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab13, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab13, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab13, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab13, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 14 -> Class O results ##################################
                classifier_label = "These are the results found by the\n classifier Minimum Distance Classifier (MDC)" \
                                   "for Class O"
                misclassification = cm_derivations["avg_misclassification"][13].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][13].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][13].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab14, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab14, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab14, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab14, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 15 -> Class P results ##################################
                classifier_label = "These are the results found by the\n classifier Minimum Distance Classifier (MDC)" \
                                   "for Class P"
                misclassification = cm_derivations["avg_misclassification"][14].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][14].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][14].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab15, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab15, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab15, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab15, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 16 -> Class Q results ##################################
                classifier_label = "These are the results found by the\n classifier Minimum Distance Classifier (MDC)" \
                                   "for Class Q"
                misclassification = cm_derivations["avg_misclassification"][15].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][15].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][15].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab16, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab16, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab16, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab16, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 17 -> Class R results ##################################
                classifier_label = "These are the results found by the\n classifier Minimum Distance Classifier (MDC)" \
                                   "for Class R"
                misclassification = cm_derivations["avg_misclassification"][16].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][16].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][16].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab17, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab17, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab17, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab17, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 18 -> Class S results ##################################
                classifier_label = "These are the results found by the\n classifier Minimum Distance Classifier (MDC)" \
                                   "for Class S"
                misclassification = cm_derivations["avg_misclassification"][17].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][17].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][17].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab18, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab18, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab18, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab18, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

            elif classifier == 2:
                # ######################## TAB 1 -> Class A results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier Fisher Discriminant Analisys (Fisher LDA) for Class A"
                misclassification = cm_derivations["avg_misclassification"][0].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][0].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][0].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab1, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab1, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab1, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab1, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 2 -> Class B results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier Fisher Discriminant Analisys (Fisher LDA) for Class B"
                misclassification = cm_derivations["avg_misclassification"][1].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][1].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][1].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab2, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab2, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab2, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab2, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 3 -> Class C results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier Fisher Discriminant Analisys (Fisher LDA) for Class C"
                misclassification = cm_derivations["avg_misclassification"][2].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][2].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][2].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab3, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab3, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab3, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab3, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 4 -> Class D results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier Fisher Discriminant Analisys (Fisher LDA) for Class D"
                misclassification = cm_derivations["avg_misclassification"][3].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][3].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][3].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab4, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab4, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab4, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab4, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 5 -> Class E results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier Fisher Discriminant Analisys (Fisher LDA) for Class E"
                misclassification = cm_derivations["avg_misclassification"][4].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][4].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][4].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab5, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab5, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab5, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab5, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 6 -> Class F results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier Fisher Discriminant Analisys (Fisher LDA) for Class F"
                misclassification = cm_derivations["avg_misclassification"][5].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][5].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][5].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab6, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab6, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab6, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab6, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 7 -> Class G results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier Fisher Discriminant Analisys (Fisher LDA) for Class G"
                misclassification = cm_derivations["avg_misclassification"][6].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][6].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][6].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab7, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab7, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab7, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab7, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 8 -> Class H results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier Fisher Discriminant Analisys (Fisher LDA) for Class H"
                misclassification = cm_derivations["avg_misclassification"][7].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][7].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][7].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab8, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab8, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab8, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab8, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 9 -> Class I results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier Fisher Discriminant Analisys (Fisher LDA) for Class I"
                misclassification = cm_derivations["avg_misclassification"][8].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][8].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][8].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab9, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab9, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab9, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab9, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 10 -> Class J results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier Fisher Discriminant Analisys (Fisher LDA) for Class J"
                misclassification = cm_derivations["avg_misclassification"][9].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][9].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][9].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab10, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab10, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab10, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab10, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 11 -> Class K results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier Fisher Discriminant Analisys (Fisher LDA) for Class K"
                misclassification = cm_derivations["avg_misclassification"][10].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][10].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][10].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab11, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab11, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab11, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab11, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 12 -> Class L results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier Fisher Discriminant Analisys (Fisher LDA) for Class L"
                misclassification = cm_derivations["avg_misclassification"][11].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][11].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][11].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab12, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab12, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab12, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab12, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 13 -> Class M results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier Fisher Discriminant Analisys (Fisher LDA) for Class M"
                misclassification = cm_derivations["avg_misclassification"][12].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][12].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][12].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab13, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab13, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab13, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab13, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 14 -> Class O results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier Fisher Discriminant Analisys (Fisher LDA) for Class O"
                misclassification = cm_derivations["avg_misclassification"][13].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][13].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][13].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab14, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab14, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab14, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab14, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 15 -> Class P results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier Fisher Discriminant Analisys (Fisher LDA) for Class P"
                misclassification = cm_derivations["avg_misclassification"][14].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][14].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][14].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab15, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab15, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab15, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab15, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 16 -> Class Q results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier Fisher Discriminant Analisys (Fisher LDA) for Class Q"
                misclassification = cm_derivations["avg_misclassification"][15].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][15].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][15].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab16, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab16, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab16, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab16, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 17 -> Class R results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier Fisher Discriminant Analisys (Fisher LDA) for Class R"
                misclassification = cm_derivations["avg_misclassification"][16].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][16].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][16].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab17, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab17, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab17, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab17, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 18 -> Class S results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier Fisher Discriminant Analisys (Fisher LDA) for Class S"
                misclassification = cm_derivations["avg_misclassification"][17].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][17].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][17].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab18, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab18, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab18, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab18, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

            elif classifier == 3:
                # ######################## TAB 1 -> Class A results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier K nearest neighbors (KNN) for class A"
                misclassification = cm_derivations["avg_misclassification"][0].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][0].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][0].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab1, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab1, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab1, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab1, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 2 -> Class B results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier K nearest neighbors (KNN) for class B"
                misclassification = cm_derivations["avg_misclassification"][1].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][1].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][1].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab2, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab2, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab2, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab2, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 3 -> Class C results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier K nearest neighbors (KNN) for class C"
                misclassification = cm_derivations["avg_misclassification"][2].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][2].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][2].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab3, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab3, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab3, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab3, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 4 -> Class D results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier K nearest neighbors (KNN) for class D"
                misclassification = cm_derivations["avg_misclassification"][3].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][3].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][3].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab4, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab4, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab4, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab4, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 5 -> Class E results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier K nearest neighbors (KNN) for class E"
                misclassification = cm_derivations["avg_misclassification"][4].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][4].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][4].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab5, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab5, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab5, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab5, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 6 -> Class F results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier K nearest neighbors (KNN) for class F"
                misclassification = cm_derivations["avg_misclassification"][5].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][5].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][5].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab6, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab6, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab6, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab6, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 7 -> Class G results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier K nearest neighbors (KNN) for class G"
                misclassification = cm_derivations["avg_misclassification"][6].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][6].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][6].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab7, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab7, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab7, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab7, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 8 -> Class H results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier K nearest neighbors (KNN) for class H"
                misclassification = cm_derivations["avg_misclassification"][7].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][7].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][7].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab8, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab8, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab8, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab8, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 9 -> Class I results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier K nearest neighbors (KNN) for class I"
                misclassification = cm_derivations["avg_misclassification"][8].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][8].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][8].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab9, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab9, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab9, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab9, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 10 -> Class J results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier K nearest neighbors (KNN) for class J"
                misclassification = cm_derivations["avg_misclassification"][9].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][9].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][9].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab10, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab10, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab10, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab10, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 11 -> Class K results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier K nearest neighbors (KNN) for class K"
                misclassification = cm_derivations["avg_misclassification"][10].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][10].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][10].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab11, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab11, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab11, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab11, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 12 -> Class L results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier K nearest neighbors (KNN) for class L"
                misclassification = cm_derivations["avg_misclassification"][11].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][11].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][11].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab12, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab12, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab12, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab12, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 13 -> Class M results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier K nearest neighbors (KNN) for class M"
                misclassification = cm_derivations["avg_misclassification"][12].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][12].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][12].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab13, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab13, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab13, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab13, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 14 -> Class O results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier K nearest neighbors (KNN) for class O"
                misclassification = cm_derivations["avg_misclassification"][13].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][13].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][13].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab14, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab14, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab14, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab14, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 15 -> Class P results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier K nearest neighbors (KNN) for class P"
                misclassification = cm_derivations["avg_misclassification"][14].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][14].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][14].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab15, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab15, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab15, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab15, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 16 -> Class Q results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier K nearest neighbors (KNN) for class Q"
                misclassification = cm_derivations["avg_misclassification"][15].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][15].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][15].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab16, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab16, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab16, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab16, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 17 -> Class R results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier K nearest neighbors (KNN) for class R"
                misclassification = cm_derivations["avg_misclassification"][16].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][16].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][16].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab17, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab17, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab17, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab17, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 18 -> Class S results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier K nearest neighbors (KNN) for class S"
                misclassification = cm_derivations["avg_misclassification"][17].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][17].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][17].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab18, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab18, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab18, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab18, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

            elif classifier == 4:
                # ######################## TAB 1 -> Class A results ##################################
                classifier_label = "These are the results found by the\n classifier Naive-Bayes for class A"
                misclassification = cm_derivations["avg_misclassification"][0].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][0].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][0].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab1, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab1, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab1, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab1, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 2 -> Class B results ##################################
                classifier_label = "These are the results found by the\n classifier Naive-Bayes for class B"
                misclassification = cm_derivations["avg_misclassification"][1].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][1].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][1].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab2, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab2, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab2, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab2, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 3 -> Class C results ##################################
                classifier_label = "These are the results found by the\n classifier Naive-Bayes for class C"
                misclassification = cm_derivations["avg_misclassification"][2].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][2].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][2].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab3, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab3, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab3, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab3, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 4 -> Class D results ##################################
                classifier_label = "These are the results found by the\n classifier Naive-Bayes for class D"
                misclassification = cm_derivations["avg_misclassification"][3].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][3].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][3].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab4, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab4, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab4, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab4, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 5 -> Class E results ##################################
                classifier_label = "These are the results found by the\n classifier Naive-Bayes for class E"
                misclassification = cm_derivations["avg_misclassification"][4].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][4].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][4].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab5, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab5, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab5, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab5, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 6 -> Class F results ##################################
                classifier_label = "These are the results found by the\n classifier Naive-Bayes for class F"
                misclassification = cm_derivations["avg_misclassification"][5].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][5].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][5].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab6, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab6, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab6, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab6, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 7 -> Class G results ##################################
                classifier_label = "These are the results found by the\n classifier Naive-Bayes for class G"
                misclassification = cm_derivations["avg_misclassification"][6].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][6].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][6].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab7, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab7, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab7, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab7, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 8 -> Class H results ##################################
                classifier_label = "These are the results found by the\n classifier Naive-Bayes for class H"
                misclassification = cm_derivations["avg_misclassification"][7].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][7].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][7].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab8, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab8, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab8, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab8, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 9 -> Class I results ##################################
                classifier_label = "These are the results found by the\n classifier Naive-Bayes for class I"
                misclassification = cm_derivations["avg_misclassification"][8].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][8].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][8].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab9, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab9, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab9, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab9, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 10 -> Class J results ##################################
                classifier_label = "These are the results found by the\n classifier Naive-Bayes for class J"
                misclassification = cm_derivations["avg_misclassification"][9].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][9].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][9].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab10, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab10, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab10, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab10, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 11 -> Class K results ##################################
                classifier_label = "These are the results found by the\n classifier Naive-Bayes for class K"
                misclassification = cm_derivations["avg_misclassification"][10].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][10].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][10].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab11, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab11, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab11, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab11, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 12 -> Class L results ##################################
                classifier_label = "These are the results found by the\n classifier Naive-Bayes for class L"
                misclassification = cm_derivations["avg_misclassification"][11].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][11].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][11].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab12, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab12, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab12, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab12, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 13 -> Class M results ##################################
                classifier_label = "These are the results found by the\n classifier Naive-Bayes for class M"
                misclassification = cm_derivations["avg_misclassification"][12].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][12].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][12].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab13, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab13, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab13, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab13, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 14 -> Class O results ##################################
                classifier_label = "These are the results found by the\n classifier Naive-Bayes for class O"
                misclassification = cm_derivations["avg_misclassification"][13].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][13].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][13].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab14, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab14, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab14, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab14, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 15 -> Class P results ##################################
                classifier_label = "These are the results found by the\n classifier Naive-Bayes for class P"
                misclassification = cm_derivations["avg_misclassification"][14].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][14].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][14].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab15, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab15, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab15, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab15, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 16 -> Class Q results ##################################
                classifier_label = "These are the results found by the\n classifier Naive-Bayes for class Q"
                misclassification = cm_derivations["avg_misclassification"][15].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][15].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][15].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab16, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab16, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab16, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab16, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 17 -> Class R results ##################################
                classifier_label = "These are the results found by the\n classifier Naive-Bayes for class R"
                misclassification = cm_derivations["avg_misclassification"][16].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][16].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][16].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab17, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab17, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab17, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab17, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 18 -> Class S results ##################################
                classifier_label = "These are the results found by the\n classifier Naive-Bayes for class S"
                misclassification = cm_derivations["avg_misclassification"][17].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][17].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][17].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab18, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab18, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab18, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab18, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

            elif classifier == 5:
                # ######################## TAB 1 -> Class A results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier Support Vector Machine (SVM) for class A"
                misclassification = cm_derivations["avg_misclassification"][0].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][0].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][0].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab1, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab1, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab1, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab1, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 2 -> Class B results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier Support Vector Machine (SVM) for class B"
                misclassification = cm_derivations["avg_misclassification"][1].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][1].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][1].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab2, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab2, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab2, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab2, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 3 -> Class C results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier Support Vector Machine (SVM) for class C"
                misclassification = cm_derivations["avg_misclassification"][2].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][2].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][2].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab3, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab3, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab3, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab3, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 4 -> Class D results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier Support Vector Machine (SVM) for class D"
                misclassification = cm_derivations["avg_misclassification"][3].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][3].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][3].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab4, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab4, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab4, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab4, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 5 -> Class E results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier Support Vector Machine (SVM) for class E"
                misclassification = cm_derivations["avg_misclassification"][4].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][4].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][4].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab5, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab5, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab5, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab5, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 6 -> Class F results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier Support Vector Machine (SVM) for class F"
                misclassification = cm_derivations["avg_misclassification"][5].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][5].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][5].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab6, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab6, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab6, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab6, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 7 -> Class G results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier Support Vector Machine (SVM) for class G"
                misclassification = cm_derivations["avg_misclassification"][6].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][6].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][6].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab7, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab7, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab7, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab7, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 8 -> Class H results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier Support Vector Machine (SVM) for class H"
                misclassification = cm_derivations["avg_misclassification"][7].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][7].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][7].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab8, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab8, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab8, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab8, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 9 -> Class I results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier Support Vector Machine (SVM) for class I"
                misclassification = cm_derivations["avg_misclassification"][8].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][8].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][8].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab9, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab9, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab9, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab9, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 10 -> Class J results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier Support Vector Machine (SVM) for class J"
                misclassification = cm_derivations["avg_misclassification"][9].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][9].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][9].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab10, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab10, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab10, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab10, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 11 -> Class K results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier Support Vector Machine (SVM) for class K"
                misclassification = cm_derivations["avg_misclassification"][10].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][10].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][10].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab11, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab11, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab11, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab11, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 12 -> Class L results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier Support Vector Machine (SVM) for class L"
                misclassification = cm_derivations["avg_misclassification"][11].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][11].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][11].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab12, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab12, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab12, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab12, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 13 -> Class M results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier Support Vector Machine (SVM) for class M"
                misclassification = cm_derivations["avg_misclassification"][12].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][12].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][12].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab13, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab13, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab13, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab13, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 14 -> Class O results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier Support Vector Machine (SVM) for class O"
                misclassification = cm_derivations["avg_misclassification"][13].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][13].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][13].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab14, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab14, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab14, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab14, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 15 -> Class P results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier Support Vector Machine (SVM) for class P"
                misclassification = cm_derivations["avg_misclassification"][14].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][14].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][14].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab15, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab15, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab15, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab15, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 16 -> Class Q results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier Support Vector Machine (SVM) for class Q"
                misclassification = cm_derivations["avg_misclassification"][15].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][15].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][15].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab16, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab16, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab16, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab16, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 17 -> Class R results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier Support Vector Machine (SVM) for class R"
                misclassification = cm_derivations["avg_misclassification"][16].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][16].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][16].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab17, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab17, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab17, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab17, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

                # ######################## TAB 18 -> Class S results ##################################
                classifier_label = "These are the results found by the\n " \
                                   "classifier Support Vector Machine (SVM) for class S"
                misclassification = cm_derivations["avg_misclassification"][17].astype(np.str)
                mean_error = "Mean of error: \n"
                mean_error += "".join(misclassification)

                result = cm_derivations["sensitivity"][17].astype(np.str)
                sensitivity = "True Positive Ratio (TPR | Sensitivity): \n"
                sensitivity += "".join(result)

                result = cm_derivations["specificity"][17].astype(np.str)
                specificity = "True Negative Ratio (TNR | Specificity): \n"
                specificity += "".join(result)

                label1 = Label(tab18, text=classifier_label, font=20)
                label1.config(anchor=CENTER)
                label1.pack(pady=15)

                label2 = Label(tab18, text=mean_error, font=20)
                label2.config(anchor=CENTER)
                label2.pack(pady=15)

                label3 = Label(tab18, text=sensitivity, font=20)
                label3.config(anchor=CENTER)
                label3.pack(pady=15)

                label4 = Label(tab18, text=specificity, font=20)
                label4.config(anchor=CENTER)
                label4.pack(pady=15)

            # Add tabs to parent container
            self.tab_parent.add(tab1, text="Class A")
            self.tab_parent.add(tab2, text="Class B")
            self.tab_parent.add(tab3, text="Class C")
            self.tab_parent.add(tab4, text="Class D")
            self.tab_parent.add(tab5, text="Class E")
            self.tab_parent.add(tab6, text="Class F")
            self.tab_parent.add(tab7, text="Class G")
            self.tab_parent.add(tab8, text="Class H")
            self.tab_parent.add(tab9, text="Class I")
            self.tab_parent.add(tab10, text="Class J")
            self.tab_parent.add(tab11, text="Class K")
            self.tab_parent.add(tab12, text="Class L")
            self.tab_parent.add(tab13, text="Class M")
            self.tab_parent.add(tab14, text="Class O")
            self.tab_parent.add(tab15, text="Class P")
            self.tab_parent.add(tab16, text="Class Q")
            self.tab_parent.add(tab17, text="Class R")
            self.tab_parent.add(tab18, text="Class S")

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
