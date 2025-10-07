import sys #Python module that provides access to specific parameters
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QComboBox, QPushButton #Imports from PyQt5 so I can develop my GUI
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow): #Code used to make the window pop up
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 1000, 1000) #Sets the size of the window
        self.setWindowTitle("League of Traders")
        self.setWindowIcon(QIcon("app.png"))
        self.setStyleSheet("""
            QMainWindow {
                background-image: url("Trading.png");
                background-repeat: no-repeat;
                background-position: center;
                background-size: cover;
            }
        """)
        central_widget = QWidget() #Creates a way to contain all widgets in window
        self.setCentralWidget(central_widget) #Tells the program all widgets must go inside main area of window
        layout = QVBoxLayout(central_widget) #Makes layout automatically vertical so it appears top to bottem
        layout.setSpacing(25) #It will automatically have my widgets be spaced out by at least 25
        central_widget.setFont(QFont("Arial", 16, QFont.Bold)) #Give all my widgets the same font so I don't have to automatically change them
        central_widget.setStyleSheet(""" #Base style for all widgets
            QPushButton, QComboBox, QLabel {
                border: 2px solid black ;
                border-radius: 5px ;
                padding: 15px 20px ;
            }
        """)

        titleLabel = QLabel("League of Traders") #Titles game league of traders
        layout.addWidget(titleLabel, alignment=Qt.AlignTop | Qt.AlignHCenter) # Align game to fit where i want it to be

        playerLabel = QLabel("Choose Number of Players:") #Some string to tell the player how many other members are in the game
        layout.addWidget(playerLabel, alignment=Qt.AlignHCenter)#Alligns it with where i want it to be

        self.player_dropdown = QComboBox() #Inital code for dropdown box
        for i in range(2,9): #For statement to give the ran of vales
            if i == 2: #If it's the smallest value
                text = "2 Player" # Output 2 players
            else:
                text = str(i) + " Players" #Otherewise do the output someone chose plus the string 'Players'
            self.player_dropdown.addItem(text) #Adds each item to the dropdown
        layout.addWidget(self.player_dropdown, alignment=Qt.AlignHCenter) #Alligns the dropdown box just under its string

        startButton = QPushButton("Start Game") #Startgame button
        startButton.setObjectName("gameButton") #Assign object name for styling
        layout.addWidget(startButton, alignment=Qt.AlignHCenter) #Allign start game

        historyButton = QPushButton("View History") #View History button
        historyButton.setObjectName("gameButton") #Assign object name for styling
        layout.addWidget(historyButton, alignment=Qt.AlignHCenter) #Allign history button

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

        startButton.clicked.connect(self.startGame) #Allows the button to be push
        historyButton.clicked.connect(self.viewHistory) #Allowes the button to be pushed

    def startGame(self):
        print("Game started with", self.player_dropdown.currentText()) #Text once you click the button

    def viewHistory(self):
        print("Viewing game history...") #Text once you click the button

def main(): #Subroutine that allows the tab to open and be in that state until users closes it
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
