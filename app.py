from PyQt6.QtWidgets import (QWidget, QVBoxLayout,
        QLabel, QApplication, QPushButton)
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt
import sys
import pyautogui
import time
from time import sleep
from threading import Thread
import socket
from subprocess import Popen

class Main(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.count = 0
        self.starttime = time.time()

    def initUI(self):
        vbox = QVBoxLayout(self)
        vbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        pixmap = QPixmap('./img/intro.jpg')
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        vbox.addWidget(lbl)
        button = QPushButton("Start taking screenshots!")
        button.setStyleSheet(
            "background-color: #262626; "
            "padding: 10px;"
            "margin: 5px;"
            "color: white;"
            "font-weight: bold;"
            "font-size: 20px;"
            "width: 60%"
        )
        button.clicked.connect(self.take_screenshot)
        vbox.addWidget(button)

        self.setLayout(vbox)

        self.move(300, 200)
        self.setWindowTitle('Too Real')
        self.setWindowIcon(QIcon('./img/favicon.ico'))

        self.show()

    def take_screenshot(self):
        #change the time
        daemon = Thread(target=self.background_task, args=(60,), daemon=True, name='Background')
        daemon.start()

    def background_task(self, interval_sec):
        while True:
            sleep(interval_sec)
            im = pyautogui.screenshot()
            im.save("./static/ss/" + str(socket.gethostname()) + str(self.count) + ".jpg")
            self.count += 1

def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    ex = Main()
    sys.exit(app.exec())


if __name__ == '__main__':
    Popen('python web.py', shell = True)    
    main()

