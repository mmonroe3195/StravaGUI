from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
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
        self.yearcombobox.setGeometry(QtCore.QRect(56, 80, 101, 22))
        self.yearcombobox.setObjectName("yearcombobox")

        for i in range(len(years) + 1):
            self.yearcombobox.addItem("")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 700, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.actComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.actComboBox.setGeometry(QtCore.QRect(235, 80, 115, 22))
        self.actComboBox.setObjectName("actComboBox")

        for i in range(len(activitytypes) + 1):
            self.actComboBox.addItem("")

        self.actComboBox.setItemText(3, "")
        self.monthComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.monthComboBox.setGeometry(QtCore.QRect(430, 80, 108, 22))
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

        self.yearlabel = QtWidgets.QLabel(self.centralwidget)
        self.yearlabel.setGeometry(QtCore.QRect(60, 60, 60, 16))
        self.yearlabel.setObjectName("yearlabel")
        self.activitylabel = QtWidgets.QLabel(self.centralwidget)
        self.activitylabel.setGeometry(QtCore.QRect(240, 60, 91, 16))
        self.activitylabel.setObjectName("activitylabel")
        self.monthlabel = QtWidgets.QLabel(self.centralwidget)
        self.monthlabel.setGeometry(QtCore.QRect(435, 60, 71, 16))
        self.monthlabel.setObjectName("monthlabel")

        self.PieChartBtn = QtWidgets.QPushButton(self.centralwidget)
        self.PieChartBtn.setGeometry(QtCore.QRect(190, 320, 91, 51))
        self.PieChartBtn.setCheckable(False)
        self.PieChartBtn.setDefault(False)
        self.PieChartBtn.setObjectName("PieChartBtn")
        self.BarGraphBtn = QtWidgets.QPushButton(self.centralwidget)
        self.BarGraphBtn.setGeometry(QtCore.QRect(300, 320, 91, 51))
        self.BarGraphBtn.setObjectName("BarGraphBtn")
        self.pieSettingComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.pieSettingComboBox.setGeometry(QtCore.QRect(10, 340, 171, 22))
        self.pieSettingComboBox.setObjectName("yearcombobox_2")
        self.pieSettingComboBox.addItem("")
        self.pieSettingComboBox.addItem("")
        self.pieSettingComboBox.addItem("")
        self.piesettinglabel = QtWidgets.QLabel(self.centralwidget)
        self.piesettinglabel.setGeometry(QtCore.QRect(17, 320, 141, 16))
        self.piesettinglabel.setObjectName("piesettinglabel")

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

        self.PieChartBtn.clicked.connect(self.pie_pressed)
        self.actComboBox.activated.connect(self.update_stats)
        self.yearcombobox.activated.connect(self.update_stats)
        self.monthComboBox.activated.connect(self.update_stats)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.update_stats()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.yearcombobox.setItemText(0, _translate("MainWindow", "All"))

        for i in range(len(years)):
            self.yearcombobox.setItemText(i + 1, _translate("MainWindow", years[i]))

        self.label.setText(_translate("MainWindow", "Select a Year,  Activity Type,  and Month to View Your Strava Statistics for it:"))
        self.actComboBox.setItemText(0, _translate("MainWindow", "All Activities"))

        for i in range(len(activitytypes)):
            self.actComboBox.setItemText(i + 1, _translate("MainWindow", activitytypes[i]))

        self.monthComboBox.setItemText(0, _translate("MainWindow", "All Months"))
        self.monthComboBox.setItemText(1, _translate("MainWindow", "Jan"))
        self.monthComboBox.setItemText(2, _translate("MainWindow", "Feb"))
        self.monthComboBox.setItemText(3, _translate("MainWindow", "March"))
        self.monthComboBox.setItemText(4, _translate("MainWindow", "April"))
        self.monthComboBox.setItemText(5, _translate("MainWindow", "May"))
        self.monthComboBox.setItemText(6, _translate("MainWindow", "June"))
        self.monthComboBox.setItemText(7, _translate("MainWindow", "July"))
        self.monthComboBox.setItemText(8, _translate("MainWindow", "Aug"))
        self.monthComboBox.setItemText(9, _translate("MainWindow", "Sept"))
        self.monthComboBox.setItemText(10, _translate("MainWindow", "Oct"))
        self.monthComboBox.setItemText(11, _translate("MainWindow", "Nov"))
        self.monthComboBox.setItemText(12, _translate("MainWindow", "Dec"))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.yearlabel.setText(_translate("MainWindow", "Year:"))
        self.activitylabel.setText(_translate("MainWindow", "Activity Type:"))
        self.monthlabel.setText(_translate("MainWindow", "Month:"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.PieChartBtn.setText(_translate("MainWindow", "Pie Chart"))
        self.BarGraphBtn.setText(_translate("MainWindow", "Bar Graph"))

        self.pieSettingComboBox.setItemText(0, _translate("MainWindow", "Activity Comparison"))
        self.pieSettingComboBox.setItemText(1, _translate("MainWindow", "Year Comparison"))
        self.pieSettingComboBox.setItemText(2, _translate("MainWindow", "Month Comparison"))
        self.piesettinglabel.setText(_translate("MainWindow", "Pie Chart Settings:"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))

    def pie_pressed(self):
        "When the PieChartBtn is clicked, this code runs to display the proper pie chart"
        _translate = QtCore.QCoreApplication.translate

        if self.yearcombobox.currentText() != "All" and self.pieSettingComboBox.currentText() == 'Year Comparison':
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setText("You can't display a pie chart that has a year comparison when you have a specific year selected.  Change the Year to 'All' and click the Pie Chart button again to proceed.")
            self.msg.setWindowTitle("Error")
            # Display the message box
            self.msg.show()

        elif self.monthComboBox.currentText() != 'All Months' and self.pieSettingComboBox.currentText() == 'Month Comparison':
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setText("You can't display a pie chart that has a month comparison when you have a specific month selected.  Change the Month to 'All Months' and click the Pie Chart button again to proceed.")
            self.msg.setWindowTitle("Error")
            # Display the message box
            self.msg.show()

        elif self.actComboBox.currentText() != 'All Activities' and self.pieSettingComboBox.currentText() == 'Activity Comparison':
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setText("You can't display a pie chart that has an activity comparison when you have a specific activity selected.  Change the Actvity to 'All Activities' and click the Pie Chart button again to proceed.")
            self.msg.setWindowTitle("Error")
            # Display the message box
            self.msg.show()
        else:
            self.msg = QMessageBox() #needed to prevent message from popping up again
            filtered = stravaposts
            #filtering data based on activities
            if self.actComboBox.currentText() != "All Activities":
                filtered = filtered[filtered.type == self.actComboBox.currentText()]

            #filtering data based on month
            if self.monthComboBox.currentText() != "All Months":
                filtered = filtered[filtered.month == self.monthComboBox.currentText()]

            #filtering data based on year
            if self.yearcombobox.currentText() != "All":
                filtered = filtered[filtered.year == self.yearcombobox.currentText()]

            #altering pie chart based on pie settings
            if self.pieSettingComboBox.currentText() == "Activity Comparison":
                pie = filtered.groupby(['type']).sum().plot(kind = 'pie', title = "Activity Comparison", y = 'distance', autopct='%1.0f%%')

            elif self.pieSettingComboBox.currentText() == "Month Comparison":
                pie = filtered.groupby(['month']).sum().plot(kind = 'pie', title = "Month Comparison", y = 'distance', autopct='%1.0f%%')

            else:
                pie = filtered.groupby(['year']).sum().plot(kind = 'pie', title = "Year Comparison", y = 'distance', autopct='%1.0f%%')

            #moving legend location so it does not overlap pie chart
            pie.legend(bbox_to_anchor=(1, 1.02))
            plt.show() #shows the pie chart

    def update_stats(self):
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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
