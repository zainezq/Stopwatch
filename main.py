import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont  # Import QFont for setting font properties


class StopwatchApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Set up the main layout
        layout = QVBoxLayout()

        # Create label to display stopwatch time
        self.label = QLabel('00:00:00', self)

        # Set the font size to a larger value
        font = QFont()
        font.setPointSize(24)  # Change the font size as needed
        self.label.setFont(font)

        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        # Create buttons for start, stop, and reset
        self.start_button = QPushButton('Start', self)
        self.start_button.clicked.connect(self.start_stopwatch)
        layout.addWidget(self.start_button)

        self.stop_button = QPushButton('Stop', self)
        self.stop_button.clicked.connect(self.stop_stopwatch)
        layout.addWidget(self.stop_button)

        self.reset_button = QPushButton('Reset', self)
        self.reset_button.clicked.connect(self.reset_stopwatch)
        layout.addWidget(self.reset_button)

        # Set up the timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)

        # Initialize variables
        self.is_running = False
        self.elapsed_time = 0

        # Set the layout and window properties
        self.setLayout(layout)
        self.setWindowTitle('Stopwatch App')
        self.setGeometry(100, 100, 400, 200)

    def start_stopwatch(self):
        if not self.is_running:
            self.is_running = True
            self.elapsed_time = 0  # Set elapsed time to zero before starting the timer
            self.timer.start(1000)  # Timer fires every 1000 ms (1 second)
            self.update_time()  # Immediately update the time

    def stop_stopwatch(self):
        if self.is_running:
            self.timer.stop()
            self.is_running = False

    def reset_stopwatch(self):
        self.timer.stop()
        self.is_running = False
        self.elapsed_time = 0
        self.update_time()

    def update_time(self):
        hours = self.elapsed_time // 3600
        minutes = (self.elapsed_time % 3600) // 60
        seconds = self.elapsed_time % 60
        time_str = f'{hours:02d}:{minutes:02d}:{seconds:02d}'
        self.label.setText(time_str)
        self.elapsed_time += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    stopwatch_app = StopwatchApp()
    stopwatch_app.show()
    sys.exit(app.exec_())
