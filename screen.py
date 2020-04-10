# Imports
from tkinter import *

# # Window Definition
first_screen = Tk()
first_screen.title("Pattern Recognition Assignment")
# first_screen['bg'] = darkBg
first_screen.geometry('600x400')
# first_screen.tk_setPalette(background=darkBg, foreground=grey)

opt_database = IntVar()

radiobutton1 = Radiobutton(first_screen, variable=opt_database, value=1, text="Accelerometer from phone").pack()
radiobutton2 = Radiobutton(first_screen, variable=opt_database, value=2, text="Gyroscope from phone").pack()
radiobutton3 = Radiobutton(first_screen, variable=opt_database, value=3, text="Accelerometer from watch").pack()
radiobutton4 = Radiobutton(first_screen, variable=opt_database, value=4, text="Gyroscope from watch").pack()

first_screen.mainloop()
