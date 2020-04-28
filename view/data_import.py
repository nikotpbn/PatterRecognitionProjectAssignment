# Imports
import tkinter as tk
from tkinter import *


# Interface to import data
class DataImport:
    # Constructor Method
    def __init__(self, *args, **kwargs):
        # Attributes
        self.background_color = "#212121"
        self.text_color = "#e0e0e0"

        # Window Definition
        self.data_import_screen = tk.Tk()
        self.data_import_screen.title("RP Assignment: Data Import")
        self.data_import_screen['bg'] = self.background_color
        self.data_import_screen.geometry("600x400")
        self.data_import_screen.tk_setPalette(
            background=self.background_color,
            foreground=self.text_color)

    # Method to create the screen design and display it
    def show(self, controller):
        # Label to show the title in the screen
        lb_title = Label(
            self.data_import_screen,
            text="Smartphone and Smartwatch Activity Recognition",
            font=20)
        lb_title.config(anchor=CENTER)
        lb_title.pack(pady=15)

        # Database Options
        opt_database = IntVar()
        database_frame = LabelFrame(
            self.data_import_screen,
            text="   Database Selection   ",
            labelanchor='n')
        database_frame.pack(pady=15)

        rb_database1 = Radiobutton(
            database_frame,
            variable=opt_database,
            value=1,
            text="Accelerometer from phone",
            selectcolor=self.background_color)
        rb_database1.grid(row=0, column=0)

        rb_database2 = Radiobutton(
            database_frame,
            variable=opt_database,
            value=2,
            text="Gyroscope from phone",
            selectcolor=self.background_color)
        rb_database2.grid(row=0, column=1)

        rb_database3 = Radiobutton(
            database_frame,
            variable=opt_database,
            value=3,
            text="Accelerometer from watch",
            selectcolor=self.background_color)
        rb_database3.grid(row=1, column=0)

        rb_database4 = Radiobutton(
            database_frame,
            variable=opt_database,
            value=4,
            text="Gyroscope from watch",
            selectcolor=self.background_color)
        rb_database4.grid(row=1, column=1)

        # Scenario Options
        opt_scenario = IntVar()
        scenario_frame = LabelFrame(
            self.data_import_screen,
            text="   Scenario Selection   ",
            labelanchor='n')
        scenario_frame.pack(pady=15)

        rb_scenario1 = Radiobutton(
            scenario_frame,
            variable=opt_scenario,
            value=1,
            text="Scenario A",
            selectcolor=self.background_color)
        rb_scenario1.grid(row=0, column=0)

        rb_scenario2 = Radiobutton(
            scenario_frame,
            variable=opt_scenario,
            value=2,
            text="Scenario B",
            selectcolor=self.background_color)
        rb_scenario2.grid(row=0, column=1)

        rb_scenario3 = Radiobutton(
            scenario_frame,
            variable=opt_scenario,
            value=3, text="Scenario C",
            selectcolor=self.background_color)
        rb_scenario3.grid(row=1, column=0, columnspan=2)

        # Execute button
        bt_run_data_import = Button(
            self.data_import_screen,
            text="Import Data",
            command=lambda: controller.data_import(
                opt_database.get(),
                opt_scenario.get()
             ))
        bt_run_data_import.config(height=3, width=50)
        bt_run_data_import.pack(pady=15)

        # Execute the screen
        self.data_import_screen.mainloop()

    # Method to destroy screen
    def dismiss(self):
        # Destroy the screen
        self.data_import_screen.destroy()
