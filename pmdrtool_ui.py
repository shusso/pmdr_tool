# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pmdrtool_ui.ui'
#
# Created: Fri Jul 22 12:12:14 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(235, 249)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.TIMERlabel = QtGui.QLabel(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TIMERlabel.sizePolicy().hasHeightForWidth())
        self.TIMERlabel.setSizePolicy(sizePolicy)
        self.TIMERlabel.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(36)
        self.TIMERlabel.setFont(font)
        self.TIMERlabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.TIMERlabel.setAutoFillBackground(False)
        self.TIMERlabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.TIMERlabel.setScaledContents(False)
        self.TIMERlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TIMERlabel.setWordWrap(False)
        self.TIMERlabel.setObjectName("TIMERlabel")
        self.verticalLayout.addWidget(self.TIMERlabel)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.STARTbutton = QtGui.QPushButton(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.STARTbutton.sizePolicy().hasHeightForWidth())
        self.STARTbutton.setSizePolicy(sizePolicy)
        self.STARTbutton.setObjectName("STARTbutton")
        self.gridLayout.addWidget(self.STARTbutton, 1, 0, 1, 1)
        self.BREAKbutton = QtGui.QPushButton(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BREAKbutton.sizePolicy().hasHeightForWidth())
        self.BREAKbutton.setSizePolicy(sizePolicy)
        self.BREAKbutton.setObjectName("BREAKbutton")
        self.gridLayout.addWidget(self.BREAKbutton, 1, 1, 1, 1)
        self.INTERNALINTbutton = QtGui.QPushButton(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.INTERNALINTbutton.sizePolicy().hasHeightForWidth())
        self.INTERNALINTbutton.setSizePolicy(sizePolicy)
        self.INTERNALINTbutton.setObjectName("INTERNALINTbutton")
        self.gridLayout.addWidget(self.INTERNALINTbutton, 2, 0, 1, 1)
        self.EXTERNALINTbutton = QtGui.QPushButton(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EXTERNALINTbutton.sizePolicy().hasHeightForWidth())
        self.EXTERNALINTbutton.setSizePolicy(sizePolicy)
        self.EXTERNALINTbutton.setObjectName("EXTERNALINTbutton")
        self.gridLayout.addWidget(self.EXTERNALINTbutton, 2, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 235, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea(QtCore.Qt.TopToolBarArea), self.toolBar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setVisible(False)
        self.actionOpen.setIconVisibleInMenu(False)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setVisible(False)
        self.actionSave.setIconVisibleInMenu(False)
        self.actionSave.setObjectName("actionSave")
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.TIMERlabel.setText(QtGui.QApplication.translate("MainWindow", "25:00", None, QtGui.QApplication.UnicodeUTF8))
        self.STARTbutton.setText(QtGui.QApplication.translate("MainWindow", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.BREAKbutton.setText(QtGui.QApplication.translate("MainWindow", "Break", None, QtGui.QApplication.UnicodeUTF8))
        self.INTERNALINTbutton.setText(QtGui.QApplication.translate("MainWindow", "Interrupt(int.)", None, QtGui.QApplication.UnicodeUTF8))
        self.EXTERNALINTbutton.setText(QtGui.QApplication.translate("MainWindow", "Interrupt(ext.)", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

