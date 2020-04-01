from tkinter import *

# Colors Definition
darkBg = '#212121'
grey = '#e0e0e0'

# Window Definition
winMenu = Tk()
winMenu.title("Dataset Choice")
winMenu['bg'] = darkBg
winMenu.geometry('600x400')

# Window Gadgets
label1 = Label(winMenu,
               text="Welcome to Rain Prediction @Australia.\nSelect below the file and the scenario to process",
               font=20)
label1['bg'] = darkBg
label1['fg'] = grey
label1.config(anchor=CENTER)
label1.pack()

r = IntVar()

radio1 = Radiobutton(winMenu, text="Binary Classifier", bg=darkBg, fg=grey, font=12, variable=r, value=1).grid(row=1, column=0)
radio2 = Radiobutton(winMenu, text="Three-class Classifier", bg=darkBg, fg=grey, font=12, variable=r, value=2).grid(row=2, column=0)

winMenu.mainloop()
