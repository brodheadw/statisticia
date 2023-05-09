#
# src/python/gui.py
#
# Created by William Brodhead
#

import tkinter as tk
from tkinter import ttk
from utils import *

class MainApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(fill=tk.BOTH, expand=True)
        self.create_widgets()

    #def create_widgets(self):

def calculate():
    # Get input values from entry widgets
    data = float(data_entry.get())

    # Call the appropriate functions for calculations
    probability_result = calc_probability(data)
    hypothesis_testing_result = hypothesis_testing(data)

    # Update the result labels with the calculated values
    probability_result_label.config(text=f"Probability: {probability_result}")
    hypothesis_testing_result_label.config(text=f"Hypothesis Testing: {hypothesis_testing_result}")

def create_gui():
    # Create the main window
    root = tk.Tk()
    root.title("Statistics Calculator")

    # Create the input fields
    data_label = ttk.Label(root, text="Data:")
    data_label.grid(column=0, row=0, padx=10, pady=10, sticky=tk.W)
    data_entry = ttk.Entry(root)
    data_entry.grid(column=1, row=0, padx=10, pady=10, sticky=tk.W)

    # Create the Calculate button
    calculate_button = ttk.Button(root, text="Calculate", command=calculate)
    calculate_button.grid(column=0, row=2, columnspan=2, pady=10)

    # Create the result labels
    probability_result_label = ttk.Label(root, text="Probability:")
    probability_result_label.grid(column=0, row=3, padx=10, pady=10, sticky=tk.W)
    hypothesis_testing_result_label = ttk.Label(root, text="Hypothesis Testing:")
    hypothesis_testing_result_label.grid(column=0, row=4, padx=10, pady=10, sticky=tk.W)

    # Start the main event loop
    root.mainloop()