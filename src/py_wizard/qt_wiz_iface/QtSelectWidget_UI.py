# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtSelectWidget_UI.ui'
#
# Created: Fri Aug 26 11:22:13 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_QtSelectWidget(object):
    def setupUi(self, QtSelectWidget):
        QtSelectWidget.setObjectName("QtSelectWidget")
        QtSelectWidget.resize(392, 132)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(QtSelectWidget.sizePolicy().hasHeightForWidth())
        QtSelectWidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(QtSelectWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.question_txt = QtGui.QLabel(QtSelectWidget)
        self.question_txt.setWordWrap(True)
        self.question_txt.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.question_txt.setObjectName("question_txt")
        self.verticalLayout.addWidget(self.question_txt)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.options_box = QtGui.QComboBox(QtSelectWidget)
        self.options_box.setObjectName("options_box")
        self.verticalLayout.addWidget(self.options_box)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.ok_btn = QtGui.QPushButton(QtSelectWidget)
        self.ok_btn.setAutoDefault(True)
        self.ok_btn.setDefault(True)
        self.ok_btn.setObjectName("ok_btn")
        self.horizontalLayout.addWidget(self.ok_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(QtSelectWidget)
        QtCore.QMetaObject.connectSlotsByName(QtSelectWidget)

    def retranslateUi(self, QtSelectWidget):
        QtSelectWidget.setWindowTitle(QtGui.QApplication.translate("QtSelectWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.question_txt.setText(QtGui.QApplication.translate("QtSelectWidget", "Question text...", None, QtGui.QApplication.UnicodeUTF8))
        self.ok_btn.setText(QtGui.QApplication.translate("QtSelectWidget", "OK", None, QtGui.QApplication.UnicodeUTF8))

