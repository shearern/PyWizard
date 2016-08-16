# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NoQuestion_UI.ui'
#
# Created: Tue Aug 16 13:38:46 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_NoQuestion(object):
    def setupUi(self, NoQuestion):
        NoQuestion.setObjectName("NoQuestion")
        NoQuestion.resize(400, 134)
        self.verticalLayout = QtGui.QVBoxLayout(NoQuestion)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(NoQuestion)
        self.label.setStyleSheet("color: rgb(136, 136, 136);")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(NoQuestion)
        QtCore.QMetaObject.connectSlotsByName(NoQuestion)

    def retranslateUi(self, NoQuestion):
        NoQuestion.setWindowTitle(QtGui.QApplication.translate("NoQuestion", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("NoQuestion", "Working ...", None, QtGui.QApplication.UnicodeUTF8))

