# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src\py_wizard\qt_console_iface\GuiConsoleMainWindow_UI.ui'
#
# Created: Tue Nov 08 13:35:41 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_GuiConsoleMainWindow(object):
    def setupUi(self, GuiConsoleMainWindow):
        GuiConsoleMainWindow.setObjectName("GuiConsoleMainWindow")
        GuiConsoleMainWindow.resize(661, 590)
        self.centralwidget = QtGui.QWidget(GuiConsoleMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.status_lbl = QtGui.QLabel(self.centralwidget)
        self.status_lbl.setObjectName("status_lbl")
        self.horizontalLayout_2.addWidget(self.status_lbl)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.log_item_container = QtGui.QScrollArea(self.centralwidget)
        self.log_item_container.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.log_item_container.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.log_item_container.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.log_item_container.setWidgetResizable(True)
        self.log_item_container.setObjectName("log_item_container")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 624, 470))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.log_item_container.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.log_item_container)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.input_txt = QtGui.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_txt.sizePolicy().hasHeightForWidth())
        self.input_txt.setSizePolicy(sizePolicy)
        self.input_txt.setMinimumSize(QtCore.QSize(0, 20))
        self.input_txt.setProperty("cursor", QtCore.Qt.IBeamCursor)
        self.input_txt.setMidLineWidth(2)
        self.input_txt.setObjectName("input_txt")
        self.horizontalLayout.addWidget(self.input_txt)
        self.quick_button_frame = QtGui.QFrame(self.centralwidget)
        self.quick_button_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.quick_button_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.quick_button_frame.setObjectName("quick_button_frame")
        self.horizontalLayout.addWidget(self.quick_button_frame)
        self.input_btn = QtGui.QPushButton(self.centralwidget)
        self.input_btn.setAutoDefault(True)
        self.input_btn.setDefault(True)
        self.input_btn.setObjectName("input_btn")
        self.horizontalLayout.addWidget(self.input_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        GuiConsoleMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(GuiConsoleMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 661, 21))
        self.menubar.setObjectName("menubar")
        GuiConsoleMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(GuiConsoleMainWindow)
        self.statusbar.setObjectName("statusbar")
        GuiConsoleMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(GuiConsoleMainWindow)
        QtCore.QMetaObject.connectSlotsByName(GuiConsoleMainWindow)

    def retranslateUi(self, GuiConsoleMainWindow):
        GuiConsoleMainWindow.setWindowTitle(QtGui.QApplication.translate("GuiConsoleMainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.status_lbl.setText(QtGui.QApplication.translate("GuiConsoleMainWindow", "Starting", None, QtGui.QApplication.UnicodeUTF8))
        self.input_btn.setText(QtGui.QApplication.translate("GuiConsoleMainWindow", "Input", None, QtGui.QApplication.UnicodeUTF8))

