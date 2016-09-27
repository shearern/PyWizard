from PySide.QtCore import *
from PySide.QtGui import *

from .NoQuestionWidget_UI import Ui_NoQuestionWidget

class NoQuestionWidget(QWidget, Ui_NoQuestionWidget):
    '''Base class for creating question widgets'''

    def __init__(self, parent):
        super(NoQuestionWidget, self).__init__(parent=parent)
        self.setupUi(self)

        # Clear placeholder text
        self.last_action_lbl.setText("")

