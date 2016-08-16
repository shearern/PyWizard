# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AnsweredQuestionWidget_UI.ui'
#
# Created: Tue Aug 16 13:38:43 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_AnsweredQuestionWidget(object):
    def setupUi(self, AnsweredQuestionWidget):
        AnsweredQuestionWidget.setObjectName("AnsweredQuestionWidget")
        AnsweredQuestionWidget.resize(400, 57)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AnsweredQuestionWidget.sizePolicy().hasHeightForWidth())
        AnsweredQuestionWidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(AnsweredQuestionWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.question_text = QtGui.QLabel(AnsweredQuestionWidget)
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        self.question_text.setFont(font)
        self.question_text.setWordWrap(True)
        self.question_text.setObjectName("question_text")
        self.verticalLayout.addWidget(self.question_text)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtGui.QLabel(AnsweredQuestionWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.answer_text = QtGui.QLabel(AnsweredQuestionWidget)
        self.answer_text.setObjectName("answer_text")
        self.horizontalLayout.addWidget(self.answer_text)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(AnsweredQuestionWidget)
        QtCore.QMetaObject.connectSlotsByName(AnsweredQuestionWidget)

    def retranslateUi(self, AnsweredQuestionWidget):
        AnsweredQuestionWidget.setWindowTitle(QtGui.QApplication.translate("AnsweredQuestionWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.question_text.setText(QtGui.QApplication.translate("AnsweredQuestionWidget", "Test Message HERE", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("AnsweredQuestionWidget", "You Answered", None, QtGui.QApplication.UnicodeUTF8))
        self.answer_text.setText(QtGui.QApplication.translate("AnsweredQuestionWidget", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

