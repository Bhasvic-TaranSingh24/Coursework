import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtCore import QTimer


class GameLauncher(QWidget):
    def __init__(self):
        super().__init__()

        self.label = QLabel("Press Start to launch the game", self)
        self.start_button = QPushButton("Start", self)

        self.start_button.clicked.connect(self.start_countdown)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.start_button)
        self.setLayout(layout)

        self.count = 3
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_label)

    def start_countdown(self):
        self.count = 3
        self.label.setText(f"My game is launching in {self.count}...")
        self.start_button.setEnabled(False)  # Disable button during countdown
        self.timer.start(1000)  # Timer timeout every 1000 ms = 1 second

    def update_label(self):
        self.count -= 1
        if self.count > 0:
            self.label.setText(f"My game is launching in {self.count}...")
        else:
            self.label.setText("Game launched!")
            self.timer.stop()
            self.start_button.setEnabled(True)  # Re-enable the button if you want


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GameLauncher()
    window.show()
    sys.exit(app.exec_())

