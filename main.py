import os
import sys

import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets

from modules import myfiles
from ui.mainwindow import Ui_MainWindow
import facebook

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("favicon.ico"))
        self.ui.SearchButton.clicked.connect(self.onSearchButtonClick)
        self.ui.DelButton.clicked.connect(self.onDelButtonClick)
        self.ui.PathButton.clicked.connect(self.OnPathButtonClick)

    def onSearchButtonClick(self):
        try:
            extension = "*."+self.ui.FileType.text()
            path = self.ui.TextPath.text()
            duplicates = myfiles.MyTable(extension, path)
            row = self.ui.DuplicatesTable.setRowCount(0)

            for i in range(len(duplicates)):
                row = self.ui.DuplicatesTable.rowCount()
                rowcheck = QtWidgets.QTableWidgetItem()
                rowcheck.setFlags(QtCore.Qt.ItemIsUserCheckable |
                                  QtCore.Qt.ItemIsEnabled)
                rowcheck.setCheckState(QtCore.Qt.Unchecked)
                row_name = QtWidgets.QTableWidgetItem(
                    duplicates.iloc[i]["Name"])
                row_size = QtWidgets.QTableWidgetItem(
                    duplicates.iloc[i]["Size"])
                row_path = QtWidgets.QTableWidgetItem(
                    duplicates.iloc[i]["Path"])
                self.ui.DuplicatesTable.insertRow(row)
                self.ui.DuplicatesTable.setItem(row, 0, rowcheck)
                self.ui.DuplicatesTable.setItem(row, 1, row_name)
                self.ui.DuplicatesTable.setItem(row, 2, row_size)
                self.ui.DuplicatesTable.setItem(row, 3, row_path)
        except:
            QtWidgets.QMessageBox.about(
                self, "Error", "Give a valid path or file type")

    def onDelButtonClick(self):

        rows = self.ui.DuplicatesTable.rowCount()
        names = []
        
        for row in range(rows):
            item = self.ui.DuplicatesTable.item(row, 0)
            # laststate = item.data(LastStateRole)
            currentState = item.checkState()
            if currentState == QtCore.Qt.Checked:
                names.append(self.ui.DuplicatesTable.item(row, 1).text())
                path = self.ui.DuplicatesTable.item(row, 3).text(
                ) + "\\" + self.ui.DuplicatesTable.item(row, 1).text()
                if os.path.exists(path):
                    os.remove(path)
                    self.ui.DuplicatesTable.setItem(
                        row, 1, QtWidgets.QTableWidgetItem(""))
                    self.ui.DuplicatesTable.setItem(
                        row, 2, QtWidgets.QTableWidgetItem(""))
                    self.ui.DuplicatesTable.setItem(
                        row, 3, QtWidgets.QTableWidgetItem(""))

        for row in range(rows):
            if self.ui.DuplicatesTable.item(row, 1).text() in names:
                self.ui.DuplicatesTable.setItem(
                    row, 1, QtWidgets.QTableWidgetItem(""))
                self.ui.DuplicatesTable.setItem(
                    row, 2, QtWidgets.QTableWidgetItem(""))
                self.ui.DuplicatesTable.setItem(
                    row, 3, QtWidgets.QTableWidgetItem(""))

        for row in reversed(range(self.ui.DuplicatesTable.rowCount())):
            name = self.ui.DuplicatesTable.item(row, 1).text()
            if name == "":
                self.ui.DuplicatesTable.removeRow(row)

    def OnPathButtonClick(self):
        name = QtWidgets.QFileDialog.getExistingDirectory(self)
        self.ui.TextPath.setText(name)


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
sys.exit(app.exec_())
