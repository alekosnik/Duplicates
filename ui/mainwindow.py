# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(512, 280)
        MainWindow.setMinimumSize(QtCore.QSize(512, 280))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(32, 32))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.SearchButton = QtWidgets.QPushButton(self.centralwidget)
        self.SearchButton.setObjectName("SearchButton")
        self.gridLayout_3.addWidget(self.SearchButton, 7, 3, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.FileType = QtWidgets.QLineEdit(self.centralwidget)
        self.FileType.setObjectName("FileType")
        self.gridLayout_3.addWidget(self.FileType, 1, 1, 1, 1)
        self.DelButton = QtWidgets.QPushButton(self.centralwidget)
        self.DelButton.setObjectName("DelButton")
        self.gridLayout_3.addWidget(self.DelButton, 7, 5, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 4, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.DuplicatesTable = QtWidgets.QTableWidget(self.centralwidget)
        self.DuplicatesTable.setAutoFillBackground(False)
        self.DuplicatesTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.DuplicatesTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.DuplicatesTable.setIconSize(QtCore.QSize(0, 0))
        self.DuplicatesTable.setObjectName("DuplicatesTable")
        self.DuplicatesTable.setColumnCount(4)
        self.DuplicatesTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.DuplicatesTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.DuplicatesTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.DuplicatesTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.DuplicatesTable.setHorizontalHeaderItem(3, item)
        self.DuplicatesTable.horizontalHeader().setVisible(True)
        self.DuplicatesTable.horizontalHeader().setCascadingSectionResizes(False)
        self.DuplicatesTable.horizontalHeader().setDefaultSectionSize(40)
        self.DuplicatesTable.horizontalHeader().setStretchLastSection(True)
        self.DuplicatesTable.verticalHeader().setVisible(False)
        self.DuplicatesTable.verticalHeader().setSortIndicatorShown(False)
        self.DuplicatesTable.verticalHeader().setStretchLastSection(False)
        self.gridLayout_3.addWidget(self.DuplicatesTable, 6, 0, 1, 7)
        self.TextPath = QtWidgets.QLineEdit(self.centralwidget)
        self.TextPath.setText("")
        self.TextPath.setObjectName("TextPath")
        self.gridLayout_3.addWidget(self.TextPath, 4, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1)
        self.PathButton = QtWidgets.QPushButton(self.centralwidget)
        self.PathButton.setObjectName("PathButton")
        self.gridLayout_3.addWidget(self.PathButton, 4, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 512, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionDocumentation = QtWidgets.QAction(MainWindow)
        self.actionDocumentation.setObjectName("actionDocumentation")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionPreferences = QtWidgets.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Duplicates"))
        self.SearchButton.setText(_translate("MainWindow", "Search"))
        self.FileType.setText(_translate("MainWindow", "mp3"))
        self.DelButton.setText(_translate("MainWindow", "Delete"))
        self.label_2.setText(_translate("MainWindow", "Path:"))
        self.DuplicatesTable.setSortingEnabled(True)
        item = self.DuplicatesTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Check"))
        item = self.DuplicatesTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.DuplicatesTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Size"))
        item = self.DuplicatesTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Path"))
        self.label.setText(_translate("MainWindow", "File Type:"))
        self.PathButton.setText(_translate("MainWindow", "Select Folder"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionDocumentation.setText(_translate("MainWindow", "Documentation"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionPreferences.setText(_translate("MainWindow", "Preferences"))
