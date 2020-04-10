# Imports
from tkinter import *
from tkinter import ttk

# Colors Definition
darkBg = '#212121'
grey = '#e0e0e0'

# Window Definition
first_screen = Tk()
first_screen.title("Pattern Recognition Assignment")
first_screen['bg'] = darkBg
first_screen.geometry('600x400')
first_screen.tk_setPalette(background=darkBg, foreground=grey)

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
scenarioFrame = LabelFrame(first_screen, text="   Select the Scenario to be used   ")
scenarioFrame.pack(pady=15)
opt_scenario = IntVar()
RBScenario1 = Radiobutton(scenarioFrame, variable=opt_scenario, value=1, text="Scenario A", selectcolor=darkBg)
RBScenario1.grid(row=0, column=0)
RBScenario2 = Radiobutton(scenarioFrame, variable=opt_scenario, value=2, text="Scenario B", selectcolor=darkBg, state=DISABLED)
RBScenario2.grid(row=0, column=1)
RBScenario3 = Radiobutton(scenarioFrame, variable=opt_scenario, value=3, text="Scenario C", selectcolor=darkBg, state=DISABLED)
RBScenario3.grid(row=1, column=0, columnspan=2)

first_screen.mainloop()
