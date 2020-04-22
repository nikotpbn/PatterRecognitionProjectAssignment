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
        self.screen_choose_classifier.geometry("600x550")
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
        self.button2 = None

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
        # Button to run the C-value or K-value test
        self.button1 = Button(
            self.screen_choose_classifier,
            text="",
            command=lambda: self.discovery_k_or_c_value(
                controller,
                opt_classifier.get()))
        self.button1.config(height=1, width=50)
        # Button to run the classifier
        self.button2 = Button(
            self.screen_choose_classifier,
            text="Get Result",
            command=lambda: controller.apply_classifier(
                int(n_runs.get()),
                int(n_subsets.get()),
                opt_classifier.get(),
                self.k_c_value.get()))
        self.button2.config(height=3, width=50)
        self.button2.pack(pady=15)

        # Execute the screen
        self.screen_choose_classifier.mainloop()

    # Method to show in the screen the C-value or K-value input and the button to run the C-value or K-value test
    def knn_svm_selected(self, classifier):
        # Test the classifier and set the right string to show
        if classifier == 3:
            self.label_knn_svm.config(text='Insert the K-value: ')
            self.button1.config(text='Run the test to see the best K value')
        else:
            self.label_knn_svm.config(text='Insert the C-value: ')
            self.button1.config(text='Run the test to see the best C value')
        # Erase the run classifier button in order to organize the information in the screen in the right way
        self.button2.pack_forget()
        # Show the frame, label and entry for C-value or K-value
        self.knn_svm_constant_frame.pack(pady=15)
        self.label_knn_svm.grid(row=0, column=0)
        self.k_c_value.grid(row=0, column=1)
        # Show the button that presents the C-value or K-value test and graphic
        self.button1.pack(pady=5)
        # Show run classifier button again
        self.button2.pack(pady=5)

    # Method to hide the inputs of C-value or K-value if the classifier selected isn't the KNN or SVM
    def other_classifier_selected(self):
        # Erase the frame, label, input and button of C-value or K-value
        self.knn_svm_constant_frame.pack_forget()
        self.label_knn_svm.grid_forget()
        self.k_c_value.grid_forget()
        self.button1.pack_forget()
        # Reconfigure the run classifier button
        self.button2.config(pady=15)

    # Method to Execute the C-value or K-value test
    def discovery_k_or_c_value(self, controller, classifier):
        # Prepare the C-value or K-value string
        if classifier == 3:
            k_c_value_str = "K-value"
        else:
            k_c_value_str = "C-value"
        # Window Definition to show the test graphic
        screen_show_k_c_value_graphic = tk.Tk()
        screen_show_k_c_value_graphic.title("RP Assignment: " + k_c_value_str + " Test")
        screen_show_k_c_value_graphic['bg'] = self.background_color
        screen_show_k_c_value_graphic.geometry("600x500")
        screen_show_k_c_value_graphic.tk_setPalette(
            background=self.background_color,
            foreground=self.text_color)

        # Call the method from controller to execute the C-value or K-value test
        k_or_c_value = controller.test_k_and_c_value(classifier)

        # Title label
        label1 = Label(
            screen_show_k_c_value_graphic,
            text="See the graphic below to choose your " + k_c_value_str,
            font=20)
        label1.config(anchor=CENTER)
        label1.pack(pady=15)

        # TODO: Show the C-value or K-value graphic

        # Just a test
        print("discovery_k_or_c_value: ", k_or_c_value)

        # Execute the screen
        screen_show_k_c_value_graphic.mainloop()

    # Method to destroy this screen
    def dismiss(self):
        # Destroy the screen
        self.screen_choose_classifier.destroy()
