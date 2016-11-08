# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GuiTaskRunner_UI.ui'
#
# Created: Fri Aug 26 11:22:11 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_GuiTaskRunner(object):
    def setupUi(self, GuiTaskRunner):
        GuiTaskRunner.setObjectName("GuiTaskRunner")
        GuiTaskRunner.resize(319, 675)
        self.centralwidget = QtGui.QWidget(GuiTaskRunner)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.question_frame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.question_frame.sizePolicy().hasHeightForWidth())
        self.question_frame.setSizePolicy(sizePolicy)
        self.question_frame.setMinimumSize(QtCore.QSize(0, 200))
        self.question_frame.setFrameShape(QtGui.QFrame.Box)
        self.question_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.question_frame.setObjectName("question_frame")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.question_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.question_widget = QtGui.QWidget(self.question_frame)
        self.question_widget.setObjectName("question_widget")
        self.verticalLayout_2.addWidget(self.question_widget)
        self.verticalLayout.addWidget(self.question_frame)
        self.log_frame = QtGui.QFrame(self.centralwidget)
        self.log_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.log_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.log_frame.setObjectName("log_frame")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.log_frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtGui.QLabel(self.log_frame)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.log_item_container = QtGui.QScrollArea(self.log_frame)
        self.log_item_container.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.log_item_container.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.log_item_container.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.log_item_container.setWidgetResizable(True)
        self.log_item_container.setObjectName("log_item_container")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 262, 369))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.log_item_container.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.log_item_container)
        self.verticalLayout.addWidget(self.log_frame)
        GuiTaskRunner.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(GuiTaskRunner)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 319, 21))
        self.menubar.setObjectName("menubar")
        GuiTaskRunner.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(GuiTaskRunner)
        self.statusbar.setObjectName("statusbar")
        GuiTaskRunner.setStatusBar(self.statusbar)

        self.retranslateUi(GuiTaskRunner)
        QtCore.QMetaObject.connectSlotsByName(GuiTaskRunner)

    def retranslateUi(self, GuiTaskRunner):
        GuiTaskRunner.setWindowTitle(QtGui.QApplication.translate("GuiTaskRunner", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("GuiTaskRunner", "Log", None, QtGui.QApplication.UnicodeUTF8))

