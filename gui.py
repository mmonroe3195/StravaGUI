from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 300, 300) #xpos, ypos, width, height (xpos is where screen shows up)
    win.setWindowTitle("Strava Viewer")

    label = QtWidgets.QLabel(win)
    label.setText("Strava View")
    label.move(50,50)

    win.show()
    sys.exit(app.exec_()) #so it exits properly

window()
