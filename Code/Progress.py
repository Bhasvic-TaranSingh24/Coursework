import sys  # Access system parameters for QApplication
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QSpinBox, QPushButton  # PyQt5 widgets
from PyQt5.QtGui import QFont, QIcon  # Font and window icon
from PyQt5.QtCore import Qt  # Alignment constants
import time  # For countdown delays

class PlayerSetupWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # Call parent QMainWindow constructor
        self.setGeometry(700, 300, 1000, 1000)  # Set window position and size
        self.setWindowTitle("League of Traders")  # Set title of the window
        self.setWindowIcon(QIcon("app.png"))  # Set window icon

        self.setStyleSheet(""" 
            QMainWindow {
                background-image: url("Trading.png");
                background-repeat: no-repeat;
                background-position: center;
                background-size: cover;
            }
        """)

        centralWidget = QWidget()  # Create central container widget
        self.setCentralWidget(centralWidget)  # Set central widget for the window

        layout = QVBoxLayout(centralWidget)  # Use vertical layout to stack widgets
        layout.setSpacing(20)  # Set spacing between widgets

        centralWidget.setFont(QFont("Arial", 16, QFont.Bold))  # Set default font for all widgets
        centralWidget.setStyleSheet("""  # Style all widgets inside central widget
               QPushButton, QLineEdit, QLabel, QSpinBox {
                font-size: 20px;  # Font size
                border: 2px solid black;  # Black border around widget
                border-radius: 5px;  # Rounded corners
                padding: 10px 15px;  # Inner padding
               }
           """)
        self.showMaximized()

        self.player_inputs = []  # Create list to store player input fields

        for i in range(6):  # Loop to create 6 player input fields
            label = QLabel("Player " + str(i + 1) + " Name:")  # Label for player
            entry = QLineEdit()  # Text input field for player name
            entry.setPlaceholderText("Enter name")  # Placeholder text for input
            layout.addWidget(label, alignment=Qt.AlignHCenter)  # Center the label horizontally
            layout.addWidget(entry, alignment=Qt.AlignHCenter)  # Center the input horizontally
            self.player_inputs.append(entry)  # Save reference to input field for later use

        capital_label = QLabel("Starting Capital (£):")  # Label for starting capital
        self.capital_input = QSpinBox()  # Input spinner for capital
        self.capital_input.setRange(1000, 50000)  # Set allowed range for capital
        self.capital_input.setValue(25000)  # Set default value
        layout.addWidget(capital_label, alignment=Qt.AlignHCenter)  # Center the label horizontally
        layout.addWidget(self.capital_input, alignment=Qt.AlignHCenter)  # Center the input horizontally

        button_layout = QHBoxLayout()  # Horizontal layout for buttons
        back_button = QPushButton("← Back")  # Back button
        forward_button = QPushButton("→ Start Game")  # Start game button
        button_layout.addWidget(back_button, alignment=Qt.AlignLeft)  # Align back button left
        button_layout.addWidget(forward_button, alignment=Qt.AlignRight)  # Align start button right

        layout.addLayout(button_layout)  # Add button layout at bottom of the vertical layout

        back_button.clicked.connect(self.go_back)  # Connect back button to go_back function
        forward_button.clicked.connect(self.start_game)  # Connect start button to start_game function

    def go_back(self):
        print("Going back...")  # Placeholder action for back button

    def start_game(self):
        print("Starting game...")  # Placeholder action for start button

def main():
    app = QApplication(sys.argv)  # Create QApplication instance
    window = PlayerSetupWindow()  # Create instance of player setup window
    window.show()  # Show the window
    sys.exit(app.exec_())  # Execute the app and exit when done

if __name__ == '__main__':
    main()  # Run main function if script is executed
