from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__() #calling parent constructor
        self.setGeometry(200, 200, 300, 300) #xpos, ypos, width, height (xpos is where screen shows up)
        self.setWindowTitle("Strava Viewer")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Strava View")
        self.label.move(50,50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click")
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("Clicked it here!!!!!!!!!!!!!!")
        self.update()

    def update(self):
        self.label.adjustSize()

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_()) #so it exits properly

window()
