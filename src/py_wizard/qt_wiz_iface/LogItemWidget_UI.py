# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LogItemWidget_UI.ui'
#
# Created: Fri Aug 26 11:55:20 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_LogItemWidget(object):
    def setupUi(self, LogItemWidget):
        LogItemWidget.setObjectName("LogItemWidget")
        LogItemWidget.resize(400, 31)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LogItemWidget.sizePolicy().hasHeightForWidth())
        LogItemWidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(LogItemWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.note = QtGui.QLabel(LogItemWidget)
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        self.note.setFont(font)
        self.note.setWordWrap(True)
        self.note.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.note.setObjectName("note")
        self.verticalLayout.addWidget(self.note)

        self.retranslateUi(LogItemWidget)
        QtCore.QMetaObject.connectSlotsByName(LogItemWidget)

    def retranslateUi(self, LogItemWidget):
        LogItemWidget.setWindowTitle(QtGui.QApplication.translate("LogItemWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.note.setText(QtGui.QApplication.translate("LogItemWidget", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

