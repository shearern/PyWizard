# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtYesNoWidget_UI.ui'
#
# Created: Fri Aug 26 11:22:15 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_QtYesNoWidget(object):
    def setupUi(self, QtYesNoWidget):
        QtYesNoWidget.setObjectName("QtYesNoWidget")
        QtYesNoWidget.resize(398, 133)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(QtYesNoWidget.sizePolicy().hasHeightForWidth())
        QtYesNoWidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(QtYesNoWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.question_txt = QtGui.QLabel(QtYesNoWidget)
        self.question_txt.setWordWrap(True)
        self.question_txt.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.question_txt.setObjectName("question_txt")
        self.verticalLayout.addWidget(self.question_txt)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.no_btn = QtGui.QPushButton(QtYesNoWidget)
        self.no_btn.setObjectName("no_btn")
        self.horizontalLayout.addWidget(self.no_btn)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.yes_btn = QtGui.QPushButton(QtYesNoWidget)
        self.yes_btn.setObjectName("yes_btn")
        self.horizontalLayout.addWidget(self.yes_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(QtYesNoWidget)
        QtCore.QMetaObject.connectSlotsByName(QtYesNoWidget)

    def retranslateUi(self, QtYesNoWidget):
        QtYesNoWidget.setWindowTitle(QtGui.QApplication.translate("QtYesNoWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.question_txt.setText(QtGui.QApplication.translate("QtYesNoWidget", "Question text...", None, QtGui.QApplication.UnicodeUTF8))
        self.no_btn.setText(QtGui.QApplication.translate("QtYesNoWidget", "No", None, QtGui.QApplication.UnicodeUTF8))
        self.yes_btn.setText(QtGui.QApplication.translate("QtYesNoWidget", "Yes", None, QtGui.QApplication.UnicodeUTF8))
