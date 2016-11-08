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

        # Set question text
        self.question_txt.setText(self.question.question_txt)

        # Set default option
        default = presenter.question.calc_default_answer()
        if default is not None:
            if default:
                self.yes_btn.setFocus()
                self.yes_btn.setDefault(True)
                self.yes_btn.setAutoDefault(True)
            else:
                self.no_btn.setFocus()
                self.no_btn.setDefault(True)
                self.no_btn.setAutoDefault(True)


    def yes_btn_pushed(self):
        self.question.set_answer(True)
        self.question_finished.emit()

    def no_btn_pushed(self):
        self.question.set_answer(False)
        self.question_finished.emit()
