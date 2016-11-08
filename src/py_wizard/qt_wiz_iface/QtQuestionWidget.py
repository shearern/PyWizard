from PySide.QtCore import *
from PySide.QtGui import *

class QtQuestionWidget(QWidget):
    '''Base class for creating question widgets'''

    question_finished = Signal()

    def __init__(self, parent, presenter):
        super(QtQuestionWidget, self).__init__(parent=parent)
        self.question_presenter = presenter

    @property
    def question(self):
        return self.question_presenter.question