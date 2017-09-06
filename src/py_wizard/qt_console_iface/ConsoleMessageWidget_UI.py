# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src\py_wizard\qt_console_iface\ConsoleMessageWidget_UI.ui'
#
# Created: Tue Nov 08 13:35:40 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ConsoleMessageWidget(object):
    def setupUi(self, ConsoleMessageWidget):
        ConsoleMessageWidget.setObjectName("ConsoleMessageWidget")
        ConsoleMessageWidget.resize(662, 29)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ConsoleMessageWidget.sizePolicy().hasHeightForWidth())
        ConsoleMessageWidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(ConsoleMessageWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.message = QtGui.QLabel(ConsoleMessageWidget)
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        self.message.setFont(font)
        self.message.setWordWrap(True)
        self.message.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.message.setObjectName("message")
        self.verticalLayout.addWidget(self.message)

        self.retranslateUi(ConsoleMessageWidget)
        QtCore.QMetaObject.connectSlotsByName(ConsoleMessageWidget)

    def retranslateUi(self, ConsoleMessageWidget):
        ConsoleMessageWidget.setWindowTitle(QtGui.QApplication.translate("ConsoleMessageWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.message.setText(QtGui.QApplication.translate("ConsoleMessageWidget", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

