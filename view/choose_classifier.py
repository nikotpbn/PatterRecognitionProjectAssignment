# Imports
import tkinter as tk
from tkinter import *


# Class to ...
class ChooseClassifier:

    # Construct method
    def __init__(self, *args, **kwargs):
        # Attributes
        self.background_color = "#212121"
        self.text_color = "#e0e0e0"

        # Window Definition
        self.screen_choose_classifier = tk.Tk()
        self.screen_choose_classifier.title("RP Assignment: Classifier selection")
        self.screen_choose_classifier['bg'] = self.background_color
        self.screen_choose_classifier.geometry("600x500")
        self.screen_choose_classifier.tk_setPalette(
            background=self.background_color,
            foreground=self.text_color)

        # Create structures to get the K and C value for KNN and SVM respectively to be add in the grid in the
        # classifier radio button event
        self.knn_svm_constant_frame = LabelFrame(
            self.screen_choose_classifier,
            text="Insert the constant value to be use by the classifier",
            labelanchor='n')
        self.label_knn_svm = Label(
            self.knn_svm_constant_frame,
            text="")
        self.k_c_value = Entry(self.knn_svm_constant_frame, width=30)
        self.button1 = None

    # Method to create the screen design and display it
    def show(self, controller):
        # Label
        label1 = Label(
            self.screen_choose_classifier,
            text="Choose the options below to run the classification",
            font=20)
        label1.config(anchor=CENTER)
        label1.pack(pady=15)
        # Classifier Options
        opt_classifier = IntVar()
        classifier_frame = LabelFrame(
            self.screen_choose_classifier,
            text="   Select the classifier   ",
            labelanchor='n')
        classifier_frame.pack(pady=15)
        rb_classifier4 = Radiobutton(
            classifier_frame,
            variable=opt_classifier,
            value=4,
            text="Bayes Classifier",
            selectcolor=self.background_color,
            command=self.other_classifier_selected)
        rb_classifier4.pack()
        rb_classifier5 = Radiobutton(
            classifier_frame,
            variable=opt_classifier,
            value=5,
            text="Support Vector Machines",
            selectcolor=self.background_color,
            command=lambda: self.knn_svm_selected(5))
        rb_classifier5.pack()
        rb_classifier3 = Radiobutton(
            classifier_frame,
            variable=opt_classifier,
            value=3,
            text="K-Nearest Neighbors (KNN)",
            selectcolor=self.background_color,
            command=lambda: self.knn_svm_selected(3))
        rb_classifier3.pack()
        rb_classifier1 = Radiobutton(
            classifier_frame,
            variable=opt_classifier,
            value=1,
            text="Minimum distance classifier (MDC)",
            selectcolor=self.background_color,
            command=self.other_classifier_selected)
        rb_classifier1.pack()
        rb_classifier2 = Radiobutton(
            classifier_frame,
            variable=opt_classifier,
            value=2,
            text="Fisher Discriminant Analisys (Fisher LDA)",
            selectcolor=self.background_color,
            command=self.other_classifier_selected)
        rb_classifier2.pack()
        # Classifier configurations
        classifier_config_frame = LabelFrame(
            self.screen_choose_classifier,
            text="   Select the configurations for the classifier   ",
            labelanchor='n')
        classifier_config_frame.pack(pady=15)
        label2 = Label(
            classifier_config_frame,
            text="Insert the number of runs:")
        label2.grid(row=0, column=0)
        n_runs = Entry(classifier_config_frame, width=30)
        n_runs.grid(row=0, column=1)
        label3 = Label(
            classifier_config_frame,
            text="Insert the number of subsets to be used in the K-fold cross-validation:     ")
        label3.grid(row=1, column=0)
        n_subsets = Entry(classifier_config_frame, width=30)
        n_subsets.grid(row=1, column=1)
        # Button to execute PCA
        self.button1 = Button(
            self.screen_choose_classifier,
            text="Get Result",
            command=lambda: controller.apply_classifier(
                n_runs.get(),
                n_subsets.get(),
                opt_classifier.get(),
                self.k_c_value.get()))
        self.button1.config(height=3, width=50)
        self.button1.pack(pady=15)

        # Execute the screen
        self.screen_choose_classifier.mainloop()

    def knn_svm_selected(self, classifier):
        # Destroy SVM entry
        if classifier == 3:
            self.label_knn_svm.config(text='Insert the K-value: ')
        else:
            self.label_knn_svm.config(text='Insert the C-value: ')
        if len(self.knn_svm_constant_frame.grid_info()) == 0 and len(self.label_knn_svm.grid_info()) == 0 and len(self.k_c_value.grid_info()) == 0:
            self.button1.pack_forget()
            self.knn_svm_constant_frame.pack(pady=15)
            self.label_knn_svm.grid(row=0, column=0)
            self.k_c_value.grid(row=0, column=1)
            self.button1.pack(pady=15)

    def other_classifier_selected(self):
        self.knn_svm_constant_frame.pack_forget()
        self.label_knn_svm.grid_forget()
        self.k_c_value.grid_forget()

    # Method to destroy this screen
    def dismiss(self):
        # Destroy the screen
        self.screen_choose_classifier.destroy()
