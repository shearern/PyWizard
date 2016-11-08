# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtSimpleWidget_UI.ui'
#
# Created: Fri Aug 26 11:22:14 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_QtSimpleWidget(object):
    def setupUi(self, QtSimpleWidget):
        QtSimpleWidget.setObjectName("QtSimpleWidget")
        QtSimpleWidget.resize(398, 132)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(QtSimpleWidget.sizePolicy().hasHeightForWidth())
        QtSimpleWidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(QtSimpleWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.question_txt = QtGui.QLabel(QtSimpleWidget)
        self.question_txt.setWordWrap(True)
        self.question_txt.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.question_txt.setObjectName("question_txt")
        self.verticalLayout.addWidget(self.question_txt)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.user_answer = QtGui.QLineEdit(QtSimpleWidget)
        self.user_answer.setObjectName("user_answer")
        self.verticalLayout.addWidget(self.user_answer)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.ok_btn = QtGui.QPushButton(QtSimpleWidget)
        self.ok_btn.setAutoDefault(True)
        self.ok_btn.setDefault(True)
        self.ok_btn.setObjectName("ok_btn")
        self.horizontalLayout.addWidget(self.ok_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(QtSimpleWidget)
        QtCore.QMetaObject.connectSlotsByName(QtSimpleWidget)

    def retranslateUi(self, QtSimpleWidget):
        QtSimpleWidget.setWindowTitle(QtGui.QApplication.translate("QtSimpleWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.question_txt.setText(QtGui.QApplication.translate("QtSimpleWidget", "Question text...", None, QtGui.QApplication.UnicodeUTF8))
        self.ok_btn.setText(QtGui.QApplication.translate("QtSimpleWidget", "OK", None, QtGui.QApplication.UnicodeUTF8))

