# Imports
from tkinter import *
from arff_dataset import Dataset


class Screens:
    # Attributes
    # Colors Definition
    darkBg = '#212121'
    grey = '#e0e0e0'
    # Info Definition
    title = "Pattern Recognition Assignment"
    size = "600x600"

    def __init__(self):
        pass

    # First Screen collect information about feature selection and feature reduction
    def main_screen(self):
        pass


# Colors Definition
darkBg = '#212121'
grey = '#e0e0e0'

# Window Definition
first_screen = Tk()
first_screen.title("Pattern Recognition Assignment")
first_screen['bg'] = darkBg
first_screen.geometry('600x600')
first_screen.tk_setPalette(background=darkBg, foreground=grey)

# Window Gadgets
label1 = Label(first_screen,
               text="Smartphone and Smartwatch Activity Recognition",
               font=20)
label1.config(anchor=CENTER)
label1.pack(pady=15)

# Database Options
databaseFrame = LabelFrame(first_screen, text="   Select the database to be used   ")
databaseFrame.pack(pady=15)
opt_database = IntVar()
RBDatabase1 = Radiobutton(databaseFrame, variable=opt_database, value=1, text="Accelerometer from phone", selectcolor=darkBg)
RBDatabase1.grid(row=0, column=0)
RBDatabase2 = Radiobutton(databaseFrame, variable=opt_database, value=2, text="Gyroscope from phone", selectcolor=darkBg)
RBDatabase2.grid(row=0, column=1)
RBDatabase3 = Radiobutton(databaseFrame, variable=opt_database, value=3, text="Accelerometer from watch", selectcolor=darkBg)
RBDatabase3.grid(row=1, column=0)
RBDatabase4 = Radiobutton(databaseFrame, variable=opt_database, value=4, text="Gyroscope from watch", selectcolor=darkBg)
RBDatabase4.grid(row=1, column=1)

# Scenario Options
scenarioFrame = LabelFrame(first_screen, text="   Select the scenario to be used   ")
scenarioFrame.pack(pady=15)
opt_scenario = IntVar()
RBScenario1 = Radiobutton(scenarioFrame, variable=opt_scenario, value=1, text="Scenario A", selectcolor=darkBg)
RBScenario1.grid(row=0, column=0)
RBScenario2 = Radiobutton(scenarioFrame, variable=opt_scenario, value=2, text="Scenario B", selectcolor=darkBg, state=DISABLED)
RBScenario2.grid(row=0, column=1)
RBScenario3 = Radiobutton(scenarioFrame, variable=opt_scenario, value=3, text="Scenario C", selectcolor=darkBg, state=DISABLED)
RBScenario3.grid(row=1, column=0, columnspan=2)

# Feature Selection Options
featureSelectionFrame = LabelFrame(first_screen, text="   Select the feature selection method to be used   ")
featureSelectionFrame.pack(pady=15)
opt_feature_selection = IntVar()
RBFeatureSelection1 = Radiobutton(featureSelectionFrame, variable=opt_feature_selection, value=1, text="K-bests", selectcolor=darkBg)
RBFeatureSelection1.pack()
RBFeatureSelection2 = Radiobutton(featureSelectionFrame, variable=opt_feature_selection, value=2, text="Kruskal-Wallis", selectcolor=darkBg)
RBFeatureSelection2.pack()

# Feature Selection Options
featureReductionFrame = LabelFrame(first_screen, text="   Select the number of features to be used   ")
featureReductionFrame.pack(pady=15)
scale1 = Scale(featureReductionFrame, from_=2, to=91, orient=HORIZONTAL, sliderlength=15, length=400, tickinterval=10)
scale1.pack()

# Execute button
button1 = Button(first_screen, text="Run Feature Selection and Feature Reduction")
button1.config(height=3, width=50)
button1.pack(pady=15)

first_screen.mainloop()
