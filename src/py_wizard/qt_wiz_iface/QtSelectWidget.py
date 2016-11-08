from PySide.QtCore import *
from PySide.QtGui import *

from QtSelectWidget_UI import Ui_QtSelectWidget
from QtQuestionWidget import QtQuestionWidget

class QtSelectWidget(QtQuestionWidget, Ui_QtSelectWidget):

    def __init__(self, parent, presenter):
        super(QtSelectWidget, self).__init__(parent=parent, presenter=presenter)
        self.setupUi(self)

        self.ok_btn.clicked.connect(self.ok_btn_pushed)
        self.ok_btn.setDefault(True)

        # Set question text
        self.question_txt.setText(presenter.question.question_txt)

        # Populate select options
#        self.options_box = QComboBox(self)
#        self.layout().addWidget(self.options_box)
        for i, option in enumerate(self.question.options):
            self.options_box.addItem(option)

        # Set default option
        default = presenter.question.calc_default_answer()
        if default is not None:
            for i, option in enumerate(self.question.options):
                if option == default:
                    self.options_box.setCurrentIndex(i)


    def ok_btn_pushed(self):
        self.question.set_answer(self.options_box.currentText())
        self.question_finished.emit()
