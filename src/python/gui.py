#
# src/python/gui.py
#
# Created by William Brodhead
#

import tkinter as tk
from tkinter import ttk

# *****************************************************************************************************************
# Main Frame

class MainFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid(column=0, row=1, padx=10, pady=10, sticky="nsew")
        self.create_widgets()

    def create_widgets(self):
        # Create the about label
        self.about_label = tk.Label(self, text="Statisticia is an application for statistical analysis.")
        self.about_label.grid(column=0, row=0, padx=10, pady=10, sticky=tk.W)

        # Create the dropdown menu
        self.option_combobox = ttk.Combobox(self, values=["--", "Probability", "Confidence Interval", "Hypothesis Test"], state="readonly")
        self.option_combobox.grid(column=0, row=1, padx=10, pady=10, sticky=tk.W)
        self.option_combobox.current(0) # Set the default option to the first option

        # Bind the dropdown menu to the on_option_change function
        self.option_combobox.bind("<<ComboboxSelected>>", lambda event: self.show_subframe(self.option_combobox.get()))

        # Create the option frame
        self.option_frame = tk.Frame(self)
        self.option_frame.grid(column=0, row=2, padx=10, pady=10, sticky="nsew")

    def show_subframe(self, frame_name):
        for widget in self.option_frame.winfo_children():
            widget.destroy() # Remove all widgets from the option frame when a new option is selected

        if frame_name == "Probability":
            probability_frame = Probability(self.option_frame)
            probability_frame.grid(column=0, row=0, sticky="nsew")
        elif frame_name == "Confidence Interval":
            confidence_interval_frame = ConfidenceInterval(self.option_frame)
            confidence_interval_frame.grid(column=0, row=0, sticky="nsew")
        elif frame_name == "Hypothesis Test":
            hypothesis_test_frame = HypothesisTest(self.option_frame)
            hypothesis_test_frame.grid(column=0, row=0, sticky="nsew")


# Show a frame in the main frame
def on_option_change(event, option_combobox, main_frame):
    selected_option = option_combobox.get()
    main_frame.show_subframe(selected_option)


# *****************************************************************************************************************
# Probability Frame

class Probability(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        # Create the probability frame
        self.formula_frame = tk.Frame(self)
        self.formula_frame.grid(column=0, row=0, sticky=tk.W, columnspan=2)

        # Create the apply button
        self.apply_button = tk.Button(self, text="Apply", command=self.on_apply)
        self.apply_button.grid(column=0, row=4, padx=10, pady=10, sticky=tk.W)

        # Create the formula label and input
        self.formula_label = tk.Label(self.formula_frame, text="Formula:")
        self.formula_label.grid(column=0, row=0, sticky=tk.W)
        self.formula_input = tk.Entry(self.formula_frame, width=20)
        self.formula_input.grid(column=1, row=0, padx=(0, 10))

        # Bind the formula input to the on_formula_entry_change function
        self.formula_input.bind('<KeyRelease>', self.on_formula_entry_change)

        # Create the probability inputs frame
        self.probability_inputs_frame = tk.Frame(self)
        self.probability_inputs_frame.grid(column=0, row=3, padx=10, pady=10, sticky=tk.W, columnspan=2)
        self.probability_inputs = {} # A dictionary of the probability input boxes

        # Add special symbols
        self.special_symbols_frame = tk.Frame(self)
        self.special_symbols_frame.grid(column=0, row=2, ipadx=0, pady=10, sticky=tk.W, columnspan=2)
        special_symbols = {'∪': '∪', '∩': '∩', '|': '|'} # Special symbols to add to the formula input

        # Create the special symbol buttons
        for i, (name, symbol) in enumerate(special_symbols.items()):
            button = tk.Button(self.special_symbols_frame, text=name, command=lambda symbol=symbol: self.insert_symbol(symbol),
                            width=1, height=2, font=('Courier', 13))
            button.grid(column=i, row=0, sticky=tk.W)

    # Insert a symbol into the formula input
    def insert_symbol(self, symbol): self.formula_input.insert(tk.INSERT, symbol)

    # Called when the apply button is pressed
    def on_apply(self):
        formula = self.formula_input.get()
        probabilities = {letter: float(widgets["entry"].get()) for letter, widgets in self.probability_inputs.items()}

        # Call the C++ function with the formula and probabilities
        result = self.master.master.master.call_cpp(formula, probabilities)
        print(result)  # For debugging

    # Called when the formula input changes
    def on_formula_entry_change(self, event):
        formula = self.formula_input.get()
        probability_letters = set([char for char in formula if char.isalpha()])

        # Remove input boxes for probabilities that are no longer in the formula
        for letter, widgets in list(self.probability_inputs.items()):
            if letter not in probability_letters:
                widgets["entry"].grid_remove()
                widgets["label"].grid_remove()
                del self.probability_inputs[letter]

        # Add input boxes for new probabilities in the formula
        for letter in probability_letters:
            if letter not in self.probability_inputs:
                row = len(self.probability_inputs)
                label = tk.Label(self.probability_inputs_frame, text=f"P({letter}):")
                label.grid(column=0, row=row, sticky=tk.W)

                entry = tk.Entry(self.probability_inputs_frame, width=5)
                entry.grid(column=1, row=row)
                self.probability_inputs[letter] = {'label': label, 'entry': entry}


# *****************************************************************************************************************
# Confidence Interval Frame

class ConfidenceInterval(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        pass
        # Add your confidence interval-specific widgets here


# *****************************************************************************************************************
# Hypothesis Test Frame

class HypothesisTest(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        pass
        # Add your hypothesis test-specific widgets here


# *****************************************************************************************************************
# Create GUI

def create_gui():
    # Create the main window
    root = tk.Tk()
    root.title("Statisticia")
    root.geometry("800x600")

    # Create the main frame
    main_frame = MainFrame(root)

    # Start the main event loop
    root.mainloop()
create_gui()