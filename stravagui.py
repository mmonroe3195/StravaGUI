from PyQt5 import QtCore, QtGui, QtWidgets
from Stravaapi import years, activitytypes, stravaposts
import matplotlib.pyplot as plt
import pandas as pd

class Ui_MainWindow(object):
    """The class for the Main UI Window"""

    def setupUi(self, MainWindow):
        """Sets up the UI"""
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(587, 426)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(200, 110, 60, 16))
        self.label1.setText("")
        self.label1.setObjectName("label1")
        self.yearcombobox = QtWidgets.QComboBox(self.centralwidget)
        self.yearcombobox.setGeometry(QtCore.QRect(10, 70, 115, 22))
        self.yearcombobox.setObjectName("yearcombobox")

        for i in range(len(years) + 1):
            self.yearcombobox.addItem("")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.actComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.actComboBox.setGeometry(QtCore.QRect(140, 70, 115, 22))
        self.actComboBox.setObjectName("actComboBox")

        for i in range(len(activitytypes) + 1):
            self.actComboBox.addItem("")

        self.actComboBox.setItemText(3, "")
        self.monthComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.monthComboBox.setGeometry(QtCore.QRect(290, 70, 115, 22))
        self.monthComboBox.setObjectName("monthComboBox")
        self.monthComboBox.addItem("")
        self.monthComboBox.addItem("")
        self.monthComboBox.addItem("")
        self.monthComboBox.addItem("")
        self.monthComboBox.addItem("")
        self.monthComboBox.addItem("")
        self.monthComboBox.addItem("")
        self.monthComboBox.addItem("")
        self.monthComboBox.addItem("")
        self.monthComboBox.addItem("")
        self.monthComboBox.addItem("")
        self.monthComboBox.addItem("")
        self.monthComboBox.addItem("")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(60, 140, 471, 145))
        self.listWidget.setObjectName("listWidget")

        for i in range(len(activitytypes) + 1):
            item = QtWidgets.QListWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.listWidget.addItem(item)

        self.StatsButton = QtWidgets.QPushButton(self.centralwidget)
        self.StatsButton.setGeometry(QtCore.QRect(440, 50, 100, 51))
        self.StatsButton.setObjectName("StatsButton")

        self.yearlabel = QtWidgets.QLabel(self.centralwidget)
        self.yearlabel.setGeometry(QtCore.QRect(16, 50, 60, 16))
        self.yearlabel.setObjectName("yearlabel")

        self.activitylabel = QtWidgets.QLabel(self.centralwidget)
        self.activitylabel.setGeometry(QtCore.QRect(146, 50, 91, 16))
        self.activitylabel.setObjectName("activitylabel")

        self.monthlabel = QtWidgets.QLabel(self.centralwidget)
        self.monthlabel.setGeometry(QtCore.QRect(296, 50, 71, 16))
        self.monthlabel.setObjectName("monthlabel")

        self.PieChartBtn = QtWidgets.QPushButton(self.centralwidget)
        self.PieChartBtn.setEnabled(False)
        self.PieChartBtn.setGeometry(QtCore.QRect(190, 320, 91, 51))
        self.PieChartBtn.setCheckable(False)
        self.PieChartBtn.setDefault(False)
        self.PieChartBtn.setObjectName("PieChartBtn")
        self.BarGraphBtn = QtWidgets.QPushButton(self.centralwidget)
        self.BarGraphBtn.setEnabled(False)
        self.BarGraphBtn.setGeometry(QtCore.QRect(300, 320, 91, 51))
        self.BarGraphBtn.setObjectName("BarGraphBtn")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 587, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())

        self.StatsButton.clicked.connect(self.stats_pressed)
        self.PieChartBtn.clicked.connect(self.pie_pressed)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.yearcombobox.setItemText(0, _translate("MainWindow", "All"))

        for i in range(len(years)):
            self.yearcombobox.setItemText(i + 1, _translate("MainWindow", years[i]))

        self.label.setText(_translate("MainWindow", "Select a Year to View Statistics for:"))
        self.actComboBox.setItemText(0, _translate("MainWindow", "All Activities"))

        for i in range(len(activitytypes)):
            self.actComboBox.setItemText(i + 1, _translate("MainWindow", activitytypes[i]))

        self.monthComboBox.setItemText(0, _translate("MainWindow", "All Months"))
        self.monthComboBox.setItemText(1, _translate("MainWindow", "01"))
        self.monthComboBox.setItemText(2, _translate("MainWindow", "02"))
        self.monthComboBox.setItemText(3, _translate("MainWindow", "03"))
        self.monthComboBox.setItemText(4, _translate("MainWindow", "04"))
        self.monthComboBox.setItemText(5, _translate("MainWindow", "05"))
        self.monthComboBox.setItemText(6, _translate("MainWindow", "06"))
        self.monthComboBox.setItemText(7, _translate("MainWindow", "07"))
        self.monthComboBox.setItemText(8, _translate("MainWindow", "08"))
        self.monthComboBox.setItemText(9, _translate("MainWindow", "09"))
        self.monthComboBox.setItemText(10, _translate("MainWindow", "10"))
        self.monthComboBox.setItemText(11, _translate("MainWindow", "11"))
        self.monthComboBox.setItemText(12, _translate("MainWindow", "12"))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.StatsButton.setText(_translate("MainWindow", "Show Stats"))
        self.yearlabel.setText(_translate("MainWindow", "Year:"))
        self.activitylabel.setText(_translate("MainWindow", "Activity Type:"))
        self.monthlabel.setText(_translate("MainWindow", "Month:"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.PieChartBtn.setText(_translate("MainWindow", "Pie Chart"))
        self.BarGraphBtn.setText(_translate("MainWindow", "Bar Graph"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))

    def pie_pressed(self):
        "When the PieChartBtn is clicked, this code runs to display the proper pie chart"
        _translate = QtCore.QCoreApplication.translate


        filtered = stravaposts
        #filtering data based on activities
        if self.actComboBox.currentText() != "All Activities":
            filtered = filtered[filtered.type == self.actComboBox.currentText()]

        if self.monthComboBox.currentText() != "All Months":
            filtered = filtered[filtered.month == self.monthComboBox.currentText()]

        if self.yearcombobox.currentText() != "All":
            filtered = filtered[filtered.year == self.yearcombobox.currentText()]

        filtered.groupby(['type']).sum().plot(kind='pie', y='distance', autopct='%1.0f%%')
        plt.show() #shows the pie chart

    def stats_pressed(self):
        """When the StatsButton is clicked, this code runs to display the proper stats"""
        _translate = QtCore.QCoreApplication.translate

        for i in range(len(activitytypes) + 1):
            item = self.listWidget.item(i)
            item.setText(_translate("MainWindow", ""))

        total_dist = 0
        distances = []
        for i in activitytypes:
            distances.append(0) #appending a 0 for each activitytype
        #the first 0 with correspond to the distance for the first activitytype
        #the second 0 will correspond to the distance for the second activitytype, etc
        for i in range(len(stravaposts['distance'])):
            if (stravaposts.at[i,'year'] == \
            self.yearcombobox.currentText() or self.yearcombobox.currentText() == "All") \
            and (stravaposts.at[i,'month'] == self.monthComboBox.currentText() \
            or self.monthComboBox.currentText() == "All Months"):
                total_dist += stravaposts.at[i,'distance']

                for j in range(len(activitytypes)):
                    if stravaposts.at[i,'type'] == activitytypes[j] \
                    and (self.actComboBox.currentText() == activitytypes[j] \
                    or self.actComboBox.currentText() == "All Activities"):
                        distances[j] += stravaposts.at[i,'distance']

        total_dist /= 1609.344 #converting meters to miles

        if(self.actComboBox.currentText() == "All Activities"):
            item = self.listWidget.item(0)
            item.setText(_translate("MainWindow", "You traveled a total distance of " + str(round(total_dist,2)) + " miles with Strava."))

        for i in range(len(distances)):
            distances[i] /= 1609.344
            if self.actComboBox.currentText() == activitytypes[i] or self.actComboBox.currentText() == "All Activities":
                item = self.listWidget.item(i + 1)
                item.setText(_translate("MainWindow", "Your " + activitytypes[i]+ " total with Strava was "+ str(round(distances[i],2)) + " miles."))

        self.PieChartBtn.setEnabled(True)
        self.BarGraphBtn.setEnabled(True)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
