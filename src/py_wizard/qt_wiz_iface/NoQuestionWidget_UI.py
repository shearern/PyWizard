# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NoQuestionWidget_UI.ui'
#
# Created: Tue Aug 16 13:41:10 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_NoQuestionWidget(object):
    def setupUi(self, NoQuestionWidget):
        NoQuestionWidget.setObjectName("NoQuestionWidget")
        NoQuestionWidget.resize(400, 134)
        self.verticalLayout = QtGui.QVBoxLayout(NoQuestionWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(NoQuestionWidget)
        self.label.setStyleSheet("color: rgb(136, 136, 136);")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(NoQuestionWidget)
        QtCore.QMetaObject.connectSlotsByName(NoQuestionWidget)

    def retranslateUi(self, NoQuestionWidget):
        NoQuestionWidget.setWindowTitle(QtGui.QApplication.translate("NoQuestionWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("NoQuestionWidget", "Working ...", None, QtGui.QApplication.UnicodeUTF8))

