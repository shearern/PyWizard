from PySide.QtCore import *
from PySide.QtGui import *

from AnsweredQuestionWidget_UI import Ui_AnsweredQuestionWidget

class AnsweredQuestionWidget(QWidget, Ui_AnsweredQuestionWidget):

    def __init__(self, parent, question_txt, answer_txt):
        super(AnsweredQuestionWidget, self).__init__(parent=parent)
        self.setupUi(self)
        self.question_text.setText(question_txt)
        self.answer_text.setText(answer_txt)

