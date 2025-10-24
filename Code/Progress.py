import sys  # Access system parameters for QApplication
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QSpinBox, QPushButton  # PyQt5 widgets
from PyQt5.QtGui import QFont, QIcon  # Font and window icon
from PyQt5.QtCore import Qt  # Alignment constants


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

        self.playerInputs = []  # Create list to store player input fields

        for i in range(6):  # Loop to create 6 player input fields
            label = QLabel("Player " + str(i + 1) + " Name:")  # Label for player
            inputField = QLineEdit()  # Text input field for player name
            inputField.context("Enter name")  # Gives context for what box does
            layout.addWidget(label, alignment=Qt.AlignHCenter)  # Center the label horizontally
            layout.addWidget(inputField, alignment=Qt.AlignHCenter)  # Center the input horizontally
            self.playerInputs.append(inputField)  # Save reference to input field for later use

        capitalLabel = QLabel("Starting Capital (£):")  # Label for starting capital
        self.capitalLabel = QSpinBox()  # Input spinner for capital
        self.capitalLabel.setRange(1000, 50000)  # Set allowed range for capital
        self.capitalLabelt.setValue(25000)  # Set default value
        layout.addWidget(capitalLabel, alignment=Qt.AlignHCenter)  # Center the label horizontally
        layout.addWidget(self.capitalLabel, alignment=Qt.AlignHCenter)  # Center the input horizontally

        buttonLayout = QHBoxLayout()  # Horizontal layout for buttons
        backButton = QPushButton("← Back")  # Back button
        forwardButton = QPushButton("→ Start Game")  # Start game button
        buttonLayout.addWidget(backButton, alignment=Qt.AlignLeft)  # Align back button left
        buttonLayout.addWidget(forwardButton, alignment=Qt.AlignRight)  # Align start button right

        layout.addLayout(buttonLayout)  # Add button layout at bottom of the vertical layout

        backButton.clicked.connect(self.goBack)  # Connect back button to goBack function
        forwardButton.clicked.connect(self.goForward)  # Connect start button to goForward function

    def goBack(self):
        print("Going back...")  # back button

    def goForward(self):
        print("Starting game...")  # start button

def main():
    app = QApplication(sys.argv)  # Create QApplication instance
    window = PlayerSetupWindow()  # Create instance of player setup window
    window.show()  # Show the window
    sys.exit(app.exec_())  # Execute the app and exit when done

if __name__ == '__main__':
    main()  # Run main function if script is executed
