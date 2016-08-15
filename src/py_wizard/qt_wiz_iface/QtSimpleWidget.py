from PySide.QtCore import *
from PySide.QtGui import *

from QtSimpleWidget_UI import Ui_QtSimpleWidget
from QtQuestionWidget import QtQuestionWidget

class QtSimpleWidget(QtQuestionWidget, Ui_QtSimpleWidget):

    def __init__(self, parent, presenter):
        super(QtSimpleWidget, self).__init__(parent=parent, presenter=presenter)
        self.setupUi(self)

        self.ok_btn.clicked.connect(self.ok_btn_pushed)
        self.ok_btn.setDefault(True)

        # Set question text
        self.question_txt.setText(presenter.question.question_txt)

        # Set default option
        default = presenter.question.calc_default_answer()
        if default is not None:
            self.user_answer.setText(str(default))

    def ok_btn_pushed(self):
        self.question.set_answer(self.user_answer.text())
        self.question_finished.emit()
