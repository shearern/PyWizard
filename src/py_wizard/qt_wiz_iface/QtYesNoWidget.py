from PySide.QtCore import *
from PySide.QtGui import *

from QtYesNoWidget_UI import Ui_QtYesNoWidget
from QtQuestionWidget import QtQuestionWidget

class QtYesNoWidget(QtQuestionWidget, Ui_QtYesNoWidget):

    def __init__(self, parent, presenter):
        super(QtYesNoWidget, self).__init__(parent=parent, presenter=presenter)
        self.setupUi(self)

        self.yes_btn.clicked.connect(self.yes_btn_pushed)
        self.no_btn.clicked.connect(self.no_btn_pushed)


    def yes_btn_pushed(self):
        self.question.set_answer(True)
        self.question_finished.emit()

    def no_btn_pushed(self):
        self.question.set_answer(False)
        self.question_finished.emit()
