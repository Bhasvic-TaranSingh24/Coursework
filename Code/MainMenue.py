import sys  # Python module that provides access to specific parameters
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QComboBox, QPushButton  # Imports from PyQt5 so I can develop my GUI
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QTimer


class MainWindow(QMainWindow):  # Code used to make the window pop up
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 1000, 1000)  # Sets the size of the window
        self.setWindowTitle("League of Traders")  # This will give the window a title screen on its top bar
        self.setWindowIcon(QIcon(
            "app.png"))  # This will give the app an image on its top bar instead of being the standard python image
        self.setStyleSheet("""
            QMainWindow {
                background-image: url("Trading.png");
                background-position: center;
                background-size: cover;

            }
        """)  # This code is used to implement a background for my screen, which is centred
        centralWidget = QWidget()  # Creates a way to contain all widgets in window
        self.setCentralWidget(centralWidget)  # Tells the program all widgets must go inside main area of window
        layout = QVBoxLayout(centralWidget)  # Makes layout automatically vertical so it appears top to bottem
        layout.setSpacing(1)  # It will automatically have my widgets be spaced out by at least 25
        centralWidget.setFont(QFont("Arial", 16,QFont.Bold))  # Give all my widgets the same font, so I don't have to automatically change them
        centralWidget.setStyleSheet(""" #Base style for all widgets
            QPushButton, QComboBox,  {
                font-size: 24px;
                border: 2px solid black ;
                border-radius: 5px ;
                padding: 15px 20px ;
            }
        """)
        titleImage = QLabel(self) #Initilise title label
        titleImage.setPixmap(QPixmap("Title.png")) #Output the title image
        layout.addWidget(titleImage, alignment=Qt.AlignTop | Qt.AlignHCenter) #Allign the label to be at a specific position
        playerLabel = QLabel(self) #Initlilise Player count label
        playerLabel.setPixmap(QPixmap("Player count.png"))
        layout.addWidget(playerLabel, alignment=Qt.AlignTop | Qt.AlignHCenter)  # Align the image to be a specific position, in this case complete




        self.showMaximized()

        self.playerDropdown = QComboBox()  # Initial code for dropdown box
        for i in range(2, 9):  # For statement to give the ran of vales
            if i == 2:  # If it's the smallest value
                text = "2 Player"  # Output 2 players
            else:
                text = str(i) + " Players"  # Otherwise do the output someone chose plus the string 'Players'
            self.playerDropdown.addItem(text)  # Adds each item to the dropdown
        layout.addWidget(self.playerDropdown,alignment=Qt.AlignAbsolute)  # Aligns the dropdown box just under its string
        self.playerDropdown.setFixedSize(800, 200)

        historyButton = QPushButton("View History")  # View History button
        historyButton.setObjectName("gameButton")  # Assign object name for styling
        layout.addWidget(historyButton, alignment=Qt.AlignHCenter)  # Align history button
        historyButton.setFixedSize(800, 200)

        startButton = QPushButton("Start Game")  # Startgame button
        startButton.setObjectName("gameButton")  # Assign object name for styling
        layout.addWidget(startButton, alignment=Qt.AlignHCenter)  # Align start game
        startButton.setFixedSize(800, 200)

        # Apply custom style for all buttons with objectName "gameButton"
        self.setStyleSheet(self.styleSheet() + """ 
            QPushButton#gameButton {
                font-size: 24px;
                font-family: Arial;
                padding: 15px 50px;
                margin: 10px;
                border: 3px solid black;
                border-radius: 15px;
                background-color: hsl(0, 100%, 64%);
                color: white;
            }
            QPushButton#gameButton:hover {
                background-color: hsl(0, 100%, 84%);
            }
        """)

        startButton.clicked.connect(self.startGame)  # Allows the button to be push
        historyButton.clicked.connect(self.viewHistory)  # Allowes the button to be pushed

    def startGame(self):
        print("Game started with", self.player_dropdown.currentText())  # Text once you click the button
        import time
        countdownButton = QLabel("League of traders")
        x = 0
        while x < 1:
            print("League of Traders will launch in 3...")
            time.sleep(2)
            print("League of Traders will launch in 2...")
            time.sleep(2)
            print("League of Traders will launch in 1...")
            time.sleep(2)
            print("League of Traders Is Launching...")
            x = x + 1

    def viewHistory(self):
        import time
        x = 0
        while x < 1:
            print("Game History will be viewed in 3...")
            time.sleep(2)
            print("Game History will be viewed in 2...")
            time.sleep(2)
            print("Game History will be viewed in 1...")
            time.sleep(2)
            print("Game History Is Being Viewed...")
            x = x + 1


def main():  # Subroutine that allows the tab to open and be in that state until users closes it
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
