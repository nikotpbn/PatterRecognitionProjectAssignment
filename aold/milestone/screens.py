# Imports
import tkinter as tk
from tkinter import *
import rp
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np


class Screens(object):
    tk = tk
    # Attributes
    # Colors Definition
    darkBg = '#212121'
    grey = '#e0e0e0'
    # Info Definition
    title = "Pattern Recognition Assignment"
    size = "600x600"
    data = []

    def __init__(self):
        # self.main_screen(self)
        pass

    # First Screen collect information about feature selection and feature reduction
    def main_screen(self, first_screen):
        # Window Definition
        first_screen.title(self.title)
        first_screen['bg'] = self.darkBg
        first_screen.geometry(self.size)
        first_screen.tk_setPalette(background=self.darkBg, foreground=self.grey)
        # Window Gadgets
        label1 = Label(first_screen, text="Smartphone and Smartwatch Activity Recognition", font=20)
        label1.config(anchor=CENTER)
        label1.pack(pady=15)
        # Database Options
        databaseFrame = LabelFrame(first_screen, text="   Select the database to be used   ")
        databaseFrame.pack(pady=15)
        opt_database = IntVar()
        RBDatabase1 = Radiobutton(databaseFrame, variable=opt_database, value=1, text="Accelerometer from phone", selectcolor=self.darkBg)
        RBDatabase1.grid(row=0, column=0)
        RBDatabase2 = Radiobutton(databaseFrame, variable=opt_database, value=2, text="Gyroscope from phone", selectcolor=self.darkBg)
        RBDatabase2.grid(row=0, column=1)
        RBDatabase3 = Radiobutton(databaseFrame, variable=opt_database, value=3, text="Accelerometer from watch", selectcolor=self.darkBg)
        RBDatabase3.grid(row=1, column=0)
        RBDatabase4 = Radiobutton(databaseFrame, variable=opt_database, value=4, text="Gyroscope from watch", selectcolor=self.darkBg)
        RBDatabase4.grid(row=1, column=1)
        # Scenario Options
        scenarioFrame = LabelFrame(first_screen, text="   Select the scenario to be used   ")
        scenarioFrame.pack(pady=15)
        opt_scenario = IntVar()
        RBScenario1 = Radiobutton(scenarioFrame, variable=opt_scenario, value=1, text="Scenario A", selectcolor=self.darkBg)
        RBScenario1.grid(row=0, column=0)
        RBScenario2 = Radiobutton(scenarioFrame, variable=opt_scenario, value=2, text="Scenario B", selectcolor=self.darkBg, state=DISABLED)
        RBScenario2.grid(row=0, column=1)
        RBScenario3 = Radiobutton(scenarioFrame, variable=opt_scenario, value=3, text="Scenario C", selectcolor=self.darkBg, state=DISABLED)
        RBScenario3.grid(row=1, column=0, columnspan=2)
        # Feature Selection Options
        featureSelectionFrame = LabelFrame(first_screen, text="   Select the feature selection method to be used   ")
        featureSelectionFrame.pack(pady=15)
        opt_feature_selection = IntVar()
        RBFeatureSelection1 = Radiobutton(featureSelectionFrame, variable=opt_feature_selection, value=1, text="K-bests", selectcolor=self.darkBg)
        RBFeatureSelection1.pack()
        RBFeatureSelection2 = Radiobutton(featureSelectionFrame, variable=opt_feature_selection, value=2, text="Kruskal-Wallis", selectcolor=self.darkBg)
        RBFeatureSelection2.pack()
        # Feature Selection Options
        featureReductionFrame = LabelFrame(first_screen, text="   Select the number of features to be used   ")
        featureReductionFrame.pack(pady=15)
        scale1 = Scale(featureReductionFrame, from_=2, to=91, orient=HORIZONTAL, sliderlength=15, length=400, tickinterval=10)
        scale1.pack()
        # Execute button
        button1 = Button(first_screen,
                         text="Run Feature Selection and Feature Reduction",
                         command=lambda: self.run_feature_selection_and_reduction(
                             opt_database.get(),
                             opt_scenario.get(),
                             opt_feature_selection.get(),
                             scale1.get()
                         ))
        button1.config(height=3, width=50)
        button1.pack(pady=15)

    def run_feature_selection_and_reduction(self, database, scenario, fr_method, n_features):
        # Change database value
        if database == 1:
            database = "PA"
        elif database == 2:
            database = "PG"
        elif database == 3:
            database = "WA"
        elif database == 4:
            database = "WG"
        # Change scenario value
        if scenario == 1:
            scenario = "A"
        elif database == 2:
            database = "B"
        elif database == 3:
            database = "C"
        self.data = rp.feature_selection_and_reduction(database, scenario, fr_method, n_features)
        # Prepare information to the screen
        if fr_method == 1:
            feature_method = "feature selection was applied with the K-bests method,\n selecting the " + \
                             str(n_features) + " and then feature reduction was applied. \n\nAs a result of applying" \
                                               " these two techniques \n" + str(len(self.data["label"])) \
                             + " were maintained and \n" + str(91 - len(self.data["label"])) + " features were retained"
        else:
            feature_method = "feature selection was applied with the Kruskal-Wallis method,\n selecting the " + \
                             str(n_features) + " and then feature reduction was applied. \n\nAs a result of applying" \
                                               " these two techniques \n" + str(len(self.data["label"])) \
                             + " were maintained and \n" + str(91 - len(self.data["label"])) + " features were retained"
        # New Screen
        second_screen = Tk()
        second_screen.title(self.title)
        second_screen['bg'] = self.darkBg
        second_screen.geometry("600x400")
        second_screen.tk_setPalette(background=self.darkBg, foreground=self.grey)
        first_screen.destroy()
        # Explanation of the run
        label1 = Label(second_screen, text=feature_method, font=20)
        label1.config(anchor=CENTER)
        label1.pack(pady=25)
        # Button to execute PCA
        button1 = Button(second_screen, text="Run PCA Analisys", command=lambda: self.run_pca(second_screen))
        button1.config(height=3, width=50)
        button1.pack(pady=15)
        # Button to dont execute PCA
        button2 = Button(second_screen, text="Skip PCA", command=lambda: self.run_classifiers(second_screen, 0))
        button2.config(height=3, width=50)
        button2.pack(pady=15)

    def run_pca(self, second_screen):
        # New Screen
        third_screen = Tk()
        third_screen.title(self.title)
        third_screen['bg'] = self.darkBg
        third_screen.geometry("1000x700")
        third_screen.tk_setPalette(background=self.darkBg, foreground=self.grey)
        second_screen.destroy()
        # PCA anaisys
        explained_variance_, x_values, singular_values_ = rp.pca_analisys(self.data)
        # Information Add
        label1 = Label(third_screen, text="Result of PCA Analisys", font=20)
        label1.config(anchor=CENTER)
        label1.grid(row=0, column=0, columnspan=2)
        # Figure Add
        figure1 = plt.Figure(figsize=(5, 4), dpi=100)
        ax1 = figure1.add_subplot(111)
        ax1.scatter(x_values, singular_values_, color='g')
        ax1.set_title('Principal Component Analysis (PCA)')
        ax1.set_xlabel('Principal Components')
        ax1.set_ylabel('Eigenvalues')
        scatter1 = FigureCanvasTkAgg(figure1, third_screen)
        scatter1.get_tk_widget().grid(row=1, column=0, pady=15)
        figure2 = plt.Figure(figsize=(5, 4), dpi=100)
        ax2 = figure2.add_subplot(111)
        ax2.scatter(x_values, (np.cumsum(explained_variance_)/sum(explained_variance_))*100, color='g')
        ax2.set_title('Principal Component Analysis (PCA)')
        ax2.set_xlabel('Principal Components')
        ax2.set_ylabel('Percentage of variance')
        scatter2 = FigureCanvasTkAgg(figure2, third_screen)
        scatter2.get_tk_widget().grid(row=1, column=1, pady=15)
        # Feature Selection Options
        pcaFrame = LabelFrame(third_screen, text="   Select the number of features to be used   ")
        pcaFrame.grid(row=2, column=0, columnspan=2, pady=15)
        scale1 = Scale(pcaFrame, from_=2, to=len(self.data["label"]), orient=HORIZONTAL, sliderlength=15, length=400, tickinterval=5)
        scale1.pack()
        # Button to execute PCA
        button1 = Button(third_screen, text="Run PCA", command=lambda: self.run_classifiers(third_screen, scale1.get()))
        button1.config(height=3, width=50)
        button1.grid(row=3, column=0, columnspan=2, pady=15)

    def run_classifiers(self, screen_to_destroy, n_features):
        screen_to_destroy.destroy()
        # New Screen
        fourth_screen = Tk()
        fourth_screen.title(self.title)
        fourth_screen['bg'] = self.darkBg
        fourth_screen.geometry("600x400")
        fourth_screen.tk_setPalette(background=self.darkBg, foreground=self.grey)
        if n_features != 0:
            self.data = rp.pca_method(self.data, n_features)
        # Label
        label1 = Label(fourth_screen, text="Choose the options below to run the classifier", font=20)
        label1.config(anchor=CENTER)
        label1.pack(pady=15)
        # Classifier Options
        classifierFrame = LabelFrame(fourth_screen, text="   Select the classifier to be used   ")
        classifierFrame.pack(pady=15)
        opt_classifier = IntVar()
        RBClassifier1 = Radiobutton(classifierFrame, variable=opt_classifier, value=3, text="KNN", selectcolor=self.darkBg)
        RBClassifier1.pack()
        RBClassifier2 = Radiobutton(classifierFrame, variable=opt_classifier, value=2, text="Fisher Discriminant Analisys (Fisher LDA)", selectcolor=self.darkBg)
        RBClassifier2.pack()
        # Classifier configurations
        classifierConfigFrame = LabelFrame(fourth_screen, text="   Select the configurations for the classifier   ")
        classifierConfigFrame.pack(pady=15)
        label2 = Label(classifierConfigFrame, text="Insert the number of runs:")
        label2.grid(row=0, column=0)
        n_runs = Entry(classifierConfigFrame, width=30)
        n_runs.grid(row=0, column=1)
        label3 = Label(classifierConfigFrame, text="Insert the number of subsets to be used in the K-fold:     ")
        label3.grid(row=1, column=0)
        n_subsets = Entry(classifierConfigFrame, width=30)
        n_subsets.grid(row=1, column=1)
        # Button to execute PCA
        button1 = Button(fourth_screen, text="Get Result", command=lambda: self.result(fourth_screen, opt_classifier.get(), n_runs.get(), n_subsets.get()))
        button1.config(height=3, width=50)
        button1.pack(pady=15)

    def result(self, screen_to_destroy, classifer, n_runs, n_subsets):
        classification_result = rp.classifier(self.data, classifer, int(n_runs), int(n_subsets))
        screen_to_destroy.destroy()
        # New Screen
        fifth_screen = Tk()
        fifth_screen.title(self.title)
        fifth_screen['bg'] = self.darkBg
        fifth_screen.geometry("600x400")
        fifth_screen.tk_setPalette(background=self.darkBg, foreground=self.grey)
        classifier_label = ""
        mean_error = ""
        true_pr = ""
        flase_pr = ""
        if classifer == 3:
            classifier_label = "These are the results found by the\n classifier KNN"
            mean_error = "Mean of errors for KNN: " + "{0:.2%}".format(classification_result["Misclassification"])
            true_pr = "True positive ratio for KNN: " + "{0:.2}".format(classification_result["Sensitivity"])
            flase_pr = "False positive ratio for KNN: " + "{0:.2}".format(classification_result["Specificity"])
        elif classifer == 2:
            classifier_label = "These are the results found by the\n classifier Fisher Discriminant Analisys (Fisher LDA)"
            mean_error = "Mean of errors Fisher LDA: " + "{0:.2%}".format(classification_result["Misclassification"])
            true_pr = "True positive ratio Fisher LDA: " + "{0:.2}".format(classification_result["Sensitivity"])
            flase_pr = "False positive ratio Fisher LDA: " + "{0:.2}".format(classification_result["Specificity"])
        # print(classification_result)
        # Information Add
        label1 = Label(fifth_screen, text=classifier_label, font=20)
        label1.config(anchor=CENTER)
        label1.pack(pady=15)
        label2 = Label(fifth_screen, text=mean_error, font=20)
        label2.config(anchor=CENTER)
        label2.pack(pady=15)
        label3 = Label(fifth_screen, text=true_pr, font=20)
        label3.config(anchor=CENTER)
        label3.pack(pady=15)
        label4 = Label(fifth_screen, text=flase_pr, font=20)
        label4.config(anchor=CENTER)
        label4.pack(pady=15)
        # Restart Application
        button1 = Button(fifth_screen, text="Restart Application", command=lambda: self.restart(fifth_screen))
        button1.config(height=3, width=50)
        button1.pack(pady=15)

    def restart(self, screen_to_destroy):
        screen_to_destroy.destroy()
        first_screen = Tk()
        app = Screens()
        app.main_screen(first_screen)
        first_screen.mainloop()


first_screen = Tk()
app = Screens()
app.main_screen(first_screen)
first_screen.mainloop()
