#
# src/python/gui.py
#
# Created by William Brodhead
#

import os
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QComboBox, QPushButton, QLineEdit, QGridLayout, QWidget, QVBoxLayout, QCheckBox, QHBoxLayout, QScrollArea

# ************************************************************************************************************
# Main Window

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Statisticia")
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        self.layout = QVBoxLayout(self.main_widget)
        self.resize(800, 600)

        self.about_label = QLabel("Statisticia is a Python-based statistical analysis application.")
        self.layout.addWidget(self.about_label)
        self.about_label.setAlignment(QtCore.Qt.AlignCenter)

        self.option_combobox = QComboBox(self)
        self.option_combobox.addItems(["--", "Probability Tools", "Confidence Interval", "Hypothesis Testing", "Regression Analysis"])
        self.layout.addWidget(self.option_combobox)
        self.option_combobox.currentIndexChanged.connect(self.show_option_window)
        self.option_combobox.setProperty("class", "option-combobox")

        self.setStyleSheet("""
            QComboBox[class="option-combobox"] {
                padding: 6px;
                max-width:200px;
            }
        """)

        self.option_window = QWidget(self)
        self.layout.addWidget(self.option_window)

    def show_option_window(self):
        self.option_window.hide()
        if self.option_combobox.currentText() == "Probability Tools":
            self.option_window = ProbabilityToolsWindow()
        elif self.option_combobox.currentText() == "Confidence Interval":
            self.option_window = ConfidenceIntervalWindow()
        elif self.option_combobox.currentText() == "Hypothesis Testing":
            self.option_window = HypothesisTestingWindow()
        elif self.option_combobox.currentText() == "Regression Analysis":
            self.option_window = RegressionAnalysisWindow()
        self.layout.addWidget(self.option_window)


# ************************************************************************************************************
# Probability Tools

class ProbabilityToolsWindow(QWidget):
    def __init__(self):
        super(ProbabilityToolsWindow, self).__init__()
        self.layout = QVBoxLayout(self)

        # Formula input
        self.formula_layout = QHBoxLayout()
        self.layout.addLayout(self.formula_layout)
        self.input_label = QLabel("Formula: ")
        self.formula_layout.addWidget(self.input_label)
        self.formula_input = QLineEdit()
        self.formula_input.setFont(QtGui.QFont("Menlo", 12))
        self.formula_layout.addWidget(self.formula_input)
        self.formula_input.textChanged.connect(self.on_formula_input_change)

        # Probability inputs
        self.probability_inputs = {}
        self.probability_inputs_layout = QGridLayout()
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area_widget = QWidget()
        self.scroll_area_widget.setLayout(self.probability_inputs_layout)
        self.scroll_area.setWidget(self.scroll_area_widget)
        self.layout.addWidget(self.scroll_area)

        self.calculate_button = QPushButton("Calculate")
        self.layout.addWidget(self.calculate_button)
        self.calculate_button.clicked.connect(self.on_calculate)

        self.output_label = QLabel("")
        self.layout.addWidget(self.output_label)

        # Special symbols
        self.special_symbols = {'∪': '∪', '∩': '∩', '|': '|'}
        self.special_symbols_layout = QHBoxLayout()
        self.formula_layout.addLayout(self.special_symbols_layout)

        for i, (name, symbol) in enumerate(self.special_symbols.items()):
            button = QPushButton(symbol)
            button.setProperty("class", "special-symbol-button")
            button.clicked.connect(lambda _, symbol=symbol: self.formula_input.insert(symbol))
            self.special_symbols_layout.addWidget(button)

        self.special_symbols_layout.addStretch()

        self.setStyleSheet("""
            QPushButton[class="special-symbol-button"] {
                font-size: 15px;
                padding: 6px;
                margin: 0px;
                min-width: 25px;
                max-width: 25px;
                min-height: 20px;
                max-height: 20px;
            }
        """)

    def on_formula_input_change(self, text):
        probability_letters = set([char for char in text if char.isalpha()])

        # Add input boxes for new probabilities in the formula
        for letter in probability_letters:
            if letter not in self.probability_inputs:
                label = QLabel(f"P({letter}):")
                row = len(self.probability_inputs)
                self.probability_inputs_layout.addWidget(label, row, 0)

                entry = QLineEdit()
                self.probability_inputs_layout.addWidget(entry, row, 1)
                self.probability_inputs[letter] = (label, entry)

        # Remove input boxes for probabilities that are no longer in the formula
        for letter, (label, widget) in list(self.probability_inputs.items()):
            if letter not in probability_letters:
                self.probability_inputs_layout.removeWidget(label)
                label.deleteLater()

                self.probability_inputs_layout.removeWidget(widget)
                widget.deleteLater()

                del self.probability_inputs[letter]

    def on_calculate(self):
        formula = self.formula_input.text()
        probabilities = {letter: float(widget.text()) for letter, (label, widget) in self.probability_inputs.items()}

        

        print(formula, probabilities)  # For debugging

# ************************************************************************************************************
# Confidence Interval

class ConfidenceIntervalWindow(QWidget):
    def __init__(self):
        super(ConfidenceIntervalWindow, self).__init__()
        self.layout = QGridLayout(self)

        self.two_tailed_checkbox = QCheckBox("Two-tailed")
        self.layout.addWidget(self.two_tailed_checkbox)

        self.input_label = QLabel("")


# ************************************************************************************************************
# Hypothesis Testing

class HypothesisTestingWindow(QWidget):
    def __init__(self):
        super(HypothesisTestingWindow, self).__init__()
        self.layout = QGridLayout(self)


# ************************************************************************************************************
# Regression Analysis

class RegressionAnalysisWindow(QWidget):
    def __init__(self):
        super(RegressionAnalysisWindow, self).__init__()
        self.layout = QGridLayout(self)


# ************************************************************************************************************
# Create GUI

def create_gui():
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()