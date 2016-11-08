from PySide.QtCore import *
from PySide.QtGui import *

from LogItemWidget_UI import Ui_LogItemWidget

class LogItemWidget(QWidget, Ui_LogItemWidget):

    def __init__(self, parent, text):
        super(LogItemWidget, self).__init__(parent=parent)
        self.setupUi(self)
        self.note.setText(text)

