# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NoQuestionWidget_UI.ui'
#
# Created: Tue Aug 16 14:05:28 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_NoQuestionWidget(object):
    def setupUi(self, NoQuestionWidget):
        NoQuestionWidget.setObjectName("NoQuestionWidget")
        NoQuestionWidget.resize(400, 134)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NoQuestionWidget.sizePolicy().hasHeightForWidth())
        NoQuestionWidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(NoQuestionWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.wokring_lbl = QtGui.QLabel(NoQuestionWidget)
        self.wokring_lbl.setStyleSheet("color: rgb(136, 136, 136);")
        self.wokring_lbl.setObjectName("wokring_lbl")
        self.verticalLayout.addWidget(self.wokring_lbl)
        self.last_action_lbl = QtGui.QLabel(NoQuestionWidget)
        self.last_action_lbl.setStyleSheet("color: rgb(136, 136, 136);")
        self.last_action_lbl.setObjectName("last_action_lbl")
        self.verticalLayout.addWidget(self.last_action_lbl)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(NoQuestionWidget)
        QtCore.QMetaObject.connectSlotsByName(NoQuestionWidget)

    def retranslateUi(self, NoQuestionWidget):
        NoQuestionWidget.setWindowTitle(QtGui.QApplication.translate("NoQuestionWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.wokring_lbl.setText(QtGui.QApplication.translate("NoQuestionWidget", "Working ...", None, QtGui.QApplication.UnicodeUTF8))
        self.last_action_lbl.setText(QtGui.QApplication.translate("NoQuestionWidget", "Last action description", None, QtGui.QApplication.UnicodeUTF8))

