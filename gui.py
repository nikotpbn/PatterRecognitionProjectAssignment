from tkinter import *
from gui_test import *

# Colors Definition
darkBg = '#212121'
grey = '#e0e0e0'

# Window Definition
winMenu = Tk()
winMenu.title("Dataset Choice")
winMenu['bg'] = darkBg
winMenu.geometry('600x400')
winMenu.tk_setPalette(background=darkBg, foreground=grey)

# Window Gadgets
label1 = Label(winMenu,
               text="Welcome to Rain Prediction @Australia.\nSelect below the file and the scenario to process",
               font=20)
label1.config(anchor=CENTER)
label1.pack()

r = StringVar()


def clicked():
    teste(r.get())


radio1 = Radiobutton(winMenu, text="Phone Accel", selectcolor='#512da8', font=12, variable=r,
                     value="Phone Accel").pack()
radio2 = Radiobutton(winMenu, text="Phone Gyro", selectcolor='#512da8', font=12, variable=r,
                     value="Phone Gyro").pack()
radio3 = Radiobutton(winMenu, text="Watch Accel", selectcolor='#512da8', font=12, variable=r,
                     value="Watch Accel").pack()
radio4 = Radiobutton(winMenu, text="Watch Gyro", selectcolor='#512da8', font=12, variable=r,
                     value="Watch Gyro").pack()

button1 = Button(winMenu, text="Click", command=clicked).pack()

winMenu.mainloop()
